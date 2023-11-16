# cython: language_level=3
#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#

# This is the main virtual machine engine for Macal.
# The code isn't pretty, but it is fast.

from __future__ import annotations
import os
import pickle
from typing import Any, Optional, Dict, List, Tuple
import importlib
import importlib.util
from collections import deque
from .bytecode_register import BytecodeRegister
from .bytecode_flags_register import BytecodeFlagsRegister
from .ast_nodetype import AstNodetype
from .python_module_info import ModuleInfo
from .config import SearchPath
from .conversion import typeFromValue
from .bytecode_debugger import ShowRegisters, ShowStack
from .runtime_scope import RuntimeScope

MAGIC_BYTES: bytes = b'BMC'
DEFAULT_MEMORY_SIZE: int = 0x100000 # 1 megabyte
FILE_FORMAT_VERSION: int = 1

class MacalVm:
    def __init__(self, filename: Optional[str] = None) -> MacalVm:
        self.filename = os.path.basename(filename) if filename is not None else None
        self.do_raise = True
        self.rax = BytecodeRegister('RAX',  0) # RAX is the aritmetic register, it's used always.
        self.rbx = BytecodeRegister('RBX',  1) # RBX is used for binary expressions.
        self.rcx = BytecodeRegister('RCX',  2) # RCX is used for loops.
        self.rdx = BytecodeRegister('RDX',  3)
        self.rsi = BytecodeRegister('RSI',  4)
        self.rdi = BytecodeRegister('RDI',  5)
        self.rbp = BytecodeRegister('RBP',  6)
        self.rsp = BytecodeRegister('RSP',  7)
        self.r8  = BytecodeRegister('R8',   8)
        self.r9  = BytecodeRegister('R9',   9)
        self.r10 = BytecodeRegister('R10', 10)
        self.r11 = BytecodeRegister('R11', 11)
        self.r12 = BytecodeRegister('R12', 12)
        self.r13 = BytecodeRegister('R13', 13)
        self.r14 = BytecodeRegister('R14', 14)
        self.r15 = BytecodeRegister('R15', 15)
        self.rip = BytecodeRegister('RIP', 16)
        self.flags = BytecodeFlagsRegister('FLAGS', 17)
        self.free_registers: List[BytecodeRegister] = [self.rdx, self.rsi, self.rdi, self.r8, self.r9, self.r10, self.r11, self.r12, self.r13, self.r14, self.r15]
        self.stack: deque = deque([(AstNodetype.INTEGER, 0), (AstNodetype.INTEGER, 0)])
        self.rsp.value = 2
        self.rbp.value = 2
        # The order in which this appears is important!
        self.opcode_to_register_map: list = [self.rax, self.rbx, self.rcx, self.rdx, self.rsi, self.rdi, self.rbp, self.rsp, self.r8, self.r9, self.r10, self.r11, self.r12, self.r13, self.r14, self.r15, self.rip, self.flags]
        # The order in which this appears is important!
        self.opcode_to_type_map : List[AstNodetype] = [AstNodetype.INTEGER, AstNodetype.FLOAT, AstNodetype.STRING, AstNodetype.BOOLEAN, AstNodetype.ARRAY, AstNodetype.RECORD, AstNodetype.VARIABLE, AstNodetype.FUNCTION,
                                   AstNodetype.TYPE, AstNodetype.NIL, AstNodetype.LIBRARY, AstNodetype.LABEL, AstNodetype.BC_METADATA, AstNodetype.STRING_INTERPOLATION_STRING_PART, AstNodetype.STRING_INTERPOLATION_END]

        self.memory : list = [None] * DEFAULT_MEMORY_SIZE
        self.Halted: bool = False
        self.Exitcode: int = 0
        self.LoadedModules: Dict[str, ModuleInfo] = {}
        self.scope: RuntimeScope = RuntimeScope()
        if filename is not None:
            self.Load(filename, 0)



    def Reset(self) -> None:
        self.free_registers = [self.rdx, self.rsi, self.rdi, self.r8, self.r9, self.r10, self.r11, self.r12, self.r13, self.r14, self.r15]
        self.stack = []
        self.memory = [None] * DEFAULT_MEMORY_SIZE
        self.Halted = False
        self.Exitcode = 0
        self.LoadedModules = {}
        self.rax.reset()
        self.rbx.reset()
        self.rcx.reset()
        self.rdx.reset()
        self.rsi.reset()
        self.rdi.reset()
        self.rbp.reset()
        self.rsp.reset()
        self.r8.reset()
        self.r9.reset()
        self.r10.reset()
        self.r11.reset()
        self.r12.reset()
        self.r13.reset()
        self.r14.reset()
        self.r15.reset()
        self.rip.reset()
        self.flags.reset()



    def Load(self, filename: str, offset: int) -> None:
        with open(filename, 'rb') as f:
            magic = f.read(3)
            if magic != MAGIC_BYTES:
                self._Error(f"File {filename} is not a valid bytecode file.")
            version = int.from_bytes(f.read(4), byteorder='little')
            if version != FILE_FORMAT_VERSION:
                self._Error(f"File {filename} is not a valid bytecode file.")
            memory_size = int.from_bytes(f.read(4), byteorder='little')
            if memory_size > DEFAULT_MEMORY_SIZE:
                self._Error(f"File {filename} is not a valid bytecode file.")
            self.memory = pickle.loads(f.read(memory_size))
            self.rip.value = offset
        self.LoadReservedVariables(self.scope)



    def SetReservedVariable(self, name: str, value: Any) -> None:
        self.scope.SetVariable(name, value)
        


    def LoadReservedVariables(self, scope: RuntimeScope) -> None:
        i = len(self.memory) - 1
        rv = i
        if self.memory[i][0] == 81:
            rv = i
        elif self.memory[i-1] == 81:
            rv = i-1
        else:
            return
        metadata = self.memory[rv][1]
        if "RESERVED" not in metadata:
            self._Error("No reserved variables found.")
        for var in metadata["RESERVED"]:
            scope.DefineVariable(var[0], var[1])



    def Save(self, filename: str, size: int) -> None:
        with open(filename, 'wb') as f:
            f.write(MAGIC_BYTES)
            f.write(FILE_FORMAT_VERSION.to_bytes(4, byteorder='little'))
            code = pickle.dumps(self.memory[:size])
            code_size = len(code)
            f.write(code_size.to_bytes(4, byteorder='little'))
            f.write(code)



    def __str__(self) -> str:
        return f"MacalVm()"



    def __repr__(self) -> str:
        return self.__str__()



    def _Error(self, message: str) -> None:
        msg = f"VM Error: {message}"
        if self.do_raise:
            raise Exception(msg)
        print(msg)
        exit(1)



    # helper functions
    def __SetFlags(self, res: Any, node_type: AstNodetype, lhs: Any, rhs: Any) -> None:
        if node_type == AstNodetype.INTEGER:
            self.flags.zero = res == 0
            self.flags.carry = res < 0
        else:
            self.flags.zero = lhs == rhs
            self.flags.carry = lhs < rhs



    def GetFreeRegister(self) -> Optional[BytecodeRegister]:
        if len(self.free_registers) == 0:
            return None
        return self.free_registers.pop()



    def ReleaseRegister(self, reg: BytecodeRegister) -> None:
        self.free_registers.append(reg)


    # execute functions
    def Execute(self):
        while True:
            opCode = self.memory[self.rip.value]
            self.rip.value += 1
            if   opCode[0] == 9 : # PUSH
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                self.stack.append((reg.value_type, reg.value))
                self.rsp.value += 1
                #ShowStack(self.stack, self.rsp, self.rbp)
            elif opCode[0] == 10: # POP
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                while len(self.stack) > self.rsp.value: self.stack.pop()
                reg.value_type, reg.value = self.stack.pop()
                self.rsp.value -= 1
                #ShowStack(self.stack, self.rsp, self.rbp)
            elif opCode[0] == 12: # MOVRI
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg.value_type = opCode[2]
                reg.value = opCode[3]
            elif opCode[0] == 58: # LOADR reg, [reg + offset]
                reg1: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg2: BytecodeRegister = self.opcode_to_register_map[opCode[2]]
                offset = opCode[3]
                reg1.value_type, reg1.value  = self.stack[reg2.value + offset]
            elif opCode[0] == 11: # MOVRR
                reg1: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg2: BytecodeRegister = self.opcode_to_register_map[opCode[2]]
                reg1.value_type, reg1.value = (reg2.value_type, reg2.value)
            elif opCode[0] == 17: # CMPRR
                reg1: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg2: BytecodeRegister = self.opcode_to_register_map[opCode[2]]
                type1 = reg1.value_type
                type2 = reg2.value_type
                value1 = reg1.value
                value2 = reg2.value
                # fix values for NIL type
                if type1 == AstNodetype.NIL:
                    value1 = AstNodetype.NIL
                if type2 == AstNodetype.NIL:
                    value2 = AstNodetype.NIL
                if type1 == AstNodetype.STRING_INTERPOLATION_STRING_PART or type1 == AstNodetype.STRING_INTERPOLATION_END:
                    type1 = AstNodetype.STRING
                if type2 == AstNodetype.STRING_INTERPOLATION_STRING_PART or type2 == AstNodetype.STRING_INTERPOLATION_END:
                    type2 = AstNodetype.STRING
                if type1 != AstNodetype.STRING and value1 == 'nil':
                    value1 = AstNodetype.NIL
                    type1 = AstNodetype.NIL
                if type2 != AstNodetype.STRING and value2 == 'nil':
                    value2 = AstNodetype.NIL
                    type2 = AstNodetype.NIL
                self.flags.zero = False
                self.flags.carry = False
                if type1 == type2:
                    if type1 == AstNodetype.INTEGER:
                        res = value1 - value2
                        self.flags.zero = res == 0
                        self.flags.carry = res < 0
                    else:
                        self.flags.zero = value1 == value2                       
                        if type1 == AstNodetype.STRING and type2 == AstNodetype.STRING:
                            self.flags.carry = reg1.value < reg2.value                        
                elif type1 == AstNodetype.NIL or type2 == AstNodetype.NIL:
                    self.flags.zero = value1 == value2
                elif type1 == AstNodetype.BOOLEAN:
                    self.flags.zero = value2 != None and value2 != 0 and value2 != False and value2 != 'nil' and value2 != AstNodetype.NIL and value1
                elif type2 == AstNodetype.BOOLEAN:
                    self.flags.zero = value1 != None and value1 != 0 and value1 != False and value1 != 'nil' and value1 != AstNodetype.NIL and value2
            elif opCode[0] == 38: # SETZR reg
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg.value = self.flags.zero is True
                reg.value_type = AstNodetype.BOOLEAN
            elif opCode[0] == 47: # RET
                self.rip.value_type, self.rip.value = self.stack.pop()
                self.rsp.value -= 1
                if self.rip.value == 0:
                    self.Halted = True
                    return -2
            elif opCode[0] == 44: # CALL addr
                self.rax.value = 0
                self.rax.value_type = AstNodetype.INTEGER
                self.stack.append((self.rax.value_type, self.rax.value)) # push return value
                self.stack.append((self.rip.value_type, self.rip.value)) # push return address
                self.rsp.value += 2
                self.rip.value = opCode[1]
            elif opCode[0] == 59: # STORR offset, reg, reg
                reg1: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                offset = opCode[2]
                reg2: BytecodeRegister = self.opcode_to_register_map[opCode[3]]
                self.stack[reg1.value + offset] = (reg2.value_type, reg2.value)
            elif opCode[0] ==  1: # JMP addr
                self.rip.value = opCode[1]
            elif opCode[0] == 33: # ORRR reg, reg
                reg1: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg2: BytecodeRegister = self.opcode_to_register_map[opCode[2]]
                reg1.value = reg1.value is True or reg2.value is True
                self.flags.zero = reg1.value is True
            elif opCode[0] == 16: # CMPRI reg, type, value
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                type1 = reg.value_type
                type2 = opCode[2]
                value = opCode[3]
                if type1 == AstNodetype.STRING_INTERPOLATION_STRING_PART or type1 == AstNodetype.STRING_INTERPOLATION_END:
                    type1 = AstNodetype.STRING
                if type2 == AstNodetype.STRING_INTERPOLATION_STRING_PART or type2 == AstNodetype.STRING_INTERPOLATION_END:
                    type2 = AstNodetype.STRING
                if type1 == type2:
                    if (type1 == AstNodetype.INTEGER):
                        res = reg.value - value
                        self.flags.zero = res == 0
                        self.flags.carry = res < 0
                    else:
                        self.flags.zero = reg.value == value
                        self.flags.carry = reg.value < value
            elif opCode[0] ==  3: # JMPNZ addr
                if self.flags.zero is False:
                    self.rip.value = opCode[1]
            elif opCode[0] == 21: # SUBRR reg, reg
                reg1: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg2: BytecodeRegister = self.opcode_to_register_map[opCode[2]]
                if reg1.value_type == reg2.value_type:
                    if reg1.value_type == AstNodetype.INTEGER:
                        self.flags.zero = reg1.value - reg2.value == 0
                        self.flags.carry = reg1.value - reg2.value < 0
                    else:
                        self.flags.zero = reg1.value == reg2.value
                        self.flags.carry = reg1.value < reg2.value
                reg1 -= reg2
            elif opCode[0] == 19: # ADDRR reg, reg
                reg1: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg2: BytecodeRegister = self.opcode_to_register_map[opCode[2]]
                if reg1.value_type == reg2.value_type:
                    if reg1.value_type == AstNodetype.INTEGER:
                        self.flags.zero = reg1.value - reg2.value == 0
                        self.flags.carry = reg1.value - reg2.value < 0
                    else:
                        self.flags.zero = reg1.value == reg2.value
                        self.flags.carry = reg1.value < reg2.value
                reg1 += reg2
            elif opCode[0] == 46: # CALLE module, function, param_count
                # call external function.
                return_value  = self.run_external_function(opCode[1], opCode[2], opCode[3])
                self.rax.value = return_value
                self.rax.value_type  = typeFromValue(return_value)
            # The opcodes below are not used in the FIB test (function5) and are in random order.
            # Need to run a sensus in more applications to optimize the order.
            elif opCode[0] == 56: # LOAD reg, offset
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg.value_type, reg.value = self.stack[opCode[2]]
            elif opCode[0] == 57: # STOR offset, reg
                #print(opCode)
                #ShowStack(self.stack, self.rsp, self.rbp)
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[2]]
                self.stack[opCode[1]] = (reg.value_type, reg.value)
            elif opCode[0] == 60: # STORIR reg1, reg2
                reg1: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg2: BytecodeRegister = self.opcode_to_register_map[opCode[2]]
                self.stack[reg1.value] = (reg2.value_type, reg2.value)
            elif opCode[0] == 82: # LOADIR reg1, reg2
                reg1: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg2: BytecodeRegister = self.opcode_to_register_map[opCode[2]]
                reg1.value_type, reg1.value = self.stack[reg2.value]
            elif opCode[0] == 69: # FEINDEX
                if self.rax.value_type == AstNodetype.RECORD:
                    lng = len(self.rax.value.keys())
                    if self.rbx.value < 0 or self.rbx.value >= lng:
                        self._Error(f"FEINDEX: Record key index out of range: {self.rbx.value} (0..{lng-1}) (RIP: {self.rip.value-1})")
                    self.rax.value = list(self.rax.value.keys())[self.rbx.value]
                else:
                    if self.rbx.value_type != AstNodetype.INTEGER:
                        self._Error(f"FEINDEX: Type error, array index must be an integer. (RIP: {self.rip.value-1})")
                    if self.rbx.value < 0 or self.rbx.value >= len(self.rax.value):
                        self._Error(f"FEINDEX: Array index out of range: {self.rbx.value} (0..{len(self.rax.value)-1}) (RIP: {self.rip.value-1})")
                    self.rax.value = self.rax.value[self.rbx.value]
                self.rax.value_type = typeFromValue(self.rax.value)
            elif opCode[0] == 68: # INDEX
                if self.rax.value_type == AstNodetype.RECORD:
                    if self.rbx.value not in self.rax.value.keys():
                        self._Error(f"INDEX: Key error: {self.rbx.value} (RIP: {self.rip.value-1})")
                    self.rax.value = self.rax.value[self.rbx.value]
                elif self.rbx.value_type != AstNodetype.INTEGER:
                    self._Error(f"INDEX: Type error, array index must be an integer. (RIP: {self.rip.value-1})")
                elif self.rbx.value < 0 or self.rbx.value >= len(self.rax.value):
                    self._Error(f"INDEX: Array index out of range: {self.rbx.value} (0..{len(self.rax.value)-1}) (RIP: {self.rip.value-1})")
                else:
                    self.rax.value = self.rax.value[self.rbx.value]
                self.rax.value_type = typeFromValue(self.rax.value)
            elif opCode[0] == 70: # INDEXR
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                if self.rax.value_type != AstNodetype.ARRAY and self.rax.value_type != AstNodetype.RECORD:
                    self._Error(f"INDEXR: Type error, can't assign to an immutable object. (RIP: {self.rip.value-1})")
                if self.rax.value_type == AstNodetype.RECORD:
                    self.rax.value[self.rbx.value] = reg.value
                else:
                    if self.rbx.value_type != AstNodetype.INTEGER:
                        self._Error(f"INDEXR: Type error, array index must be an integer. (RIP: {self.rip.value-1})")
                    if self.rbx.value < 0 or self.rbx.value >= len(self.rax.value):
                        self._Error(f"INDEXR: Index out of range: {self.rbx.value} (0..{len(self.rax.value)-1}) (RIP: {self.rip.value-1})")
                    self.rax.value[self.rbx.value] = reg.value
                self.rax.value_type = typeFromValue(self.rax.value)
            elif opCode[0] == 63: # APPEND reg1, reg2
                reg1: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg2: BytecodeRegister = self.opcode_to_register_map[opCode[2]]
                if reg1.value_type != AstNodetype.ARRAY:
                    self._Error(f"APPEND: Type error, can't append to an immutable object. (RIP: {self.rip.value-1})")
                reg1.value.append(reg2.value)
            elif opCode[0] == 39: # SETNZR reg
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg.value = self.flags.zero is False
                reg.value_type = AstNodetype.BOOLEAN
            elif opCode[0] == 40: # SETLR reg
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg.value = self.flags.carry is True and self.flags.zero is False
                reg.value_type = AstNodetype.BOOLEAN
            elif opCode[0] == 41: # SETGR reg
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg.value = self.flags.carry is False and self.flags.zero is False
                reg.value_type = AstNodetype.BOOLEAN
            elif opCode[0] == 42: # SETLER reg
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg.value = self.flags.carry is True or self.flags.zero is True
                reg.value_type = AstNodetype.BOOLEAN
            elif opCode[0] == 43: # SETGER reg
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg.value = self.flags.carry is False or self.flags.zero is True
                reg.value_type = AstNodetype.BOOLEAN
            elif opCode[0] == 35: # XOR reg, reg
                reg1: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg2: BytecodeRegister = self.opcode_to_register_map[opCode[2]]
                reg1 ^= reg2
                self.flags.zero = reg1.value == 0
            elif opCode[0] == 45: # CALLR reg
                reg = self.opcode_to_register_map[opCode[1]]
                self.rax.reset()
                self.stack.append((self.rax.value_type, self.rax.value)) # push return value
                self.stack.append((self.rip.value_type, self.rip.value)) # push return address
                self.rsp.value += 2
                self.rip.value = reg.value
            elif opCode[0] == 67: # PRNT
                value = f"{self.rax.value}"
                if self.rax.value_type == AstNodetype.NIL or self.rax.value == AstNodetype.NIL:
                    value = "nil"
                elif self.rax.value_type == AstNodetype.BOOLEAN:
                    value = "true" if self.rax.value == 1 else "false"
                elif self.rax.value_type == AstNodetype.TYPE:
                    value = f"{self.opcode_to_type_map[self.rax.value-128].name.lower() }"
                print(f"{value}", end='')
            elif opCode[0] == 2: # JMPZ addr
                if self.flags.zero == True:
                    self.rip.value = opCode[1]
            elif opCode[0] == 4: # JMPLT addr
                if self.flags.zero == False and self.flags.carry == True:
                    self.rip.value = opCode[1]
            elif opCode[0] == 5: # JMPGT addr
                if self.flags.zero == False and self.flags.carry == False:
                    self.rip.value = opCode[1]
            elif opCode[0] == 6: # JMPLTE addr
                if (self.flags.zero == False and self.flags.carry == True) or (self.flags.zero == True and self.flags.carry == False):
                    self.rip.value = opCode[1]
            elif opCode[0] == 7: # JMPGTE addr
                if (self.flags.zero == False and self.flags.carry == False) or (self.flags.zero == True and self.flags.carry == False):
                    self.rip.value = opCode[1]
            elif opCode[0] == 13: # MOVMI [addr], type, value
                self.memory[opCode[1]] = (opCode[2], opCode[3])
            elif opCode[0] == 15: # MOVMR [addr], reg
                self.memory[opCode[1]] = (reg.value_type, reg.value)
            elif opCode[0] == 14: # MOVRM reg, [addr]
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg.value_type, reg.value = self.memory[opCode[2]]
            elif opCode[0] == 34: # XORI
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                tmp = BytecodeRegister('tmp', 0)
                tmp.value_type, tmp.value = (opCode[2], opCode[3])
                reg ^= tmp
                self.flags.zero = reg.value == 0
            elif opCode[0] == 48: # RETZ
                if self.flags.zero == True:
                    self.rip.value_type, self.rip.value = self.stack.pop()
                    self.rsp.value -= 1
                    if self.rip == 0:
                        self.Halted = True
                        return -2
            elif opCode[0] == 49: # RETNZ
                if self.flags.zero == False:
                    self.rip.value_type, self.rip.value = self.stack.pop()
                    self.rsp.value -= 1
                    if self.rip == 0:
                        self.Halted = True
                        return -2
            elif opCode[0] == 50: # HALT
                self.Halted = True
                return -2
            elif opCode[0] == 36: # NEG
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg.value = -reg.value
            elif opCode[0] == 37: # NOT
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg.value = not reg.value
            elif opCode[0] == 18: # ADDRI reg, type, value
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg.value_type, reg.value = (opCode[2], opCode[3])
            elif opCode[0] == 21: # SUBRR reg, reg
                reg1: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg2: BytecodeRegister = self.opcode_to_register_map[opCode[2]]
                self.__SetFlags(reg1.value - reg2.value, reg1.value_type, reg1.value, reg2.value)
                reg1 -= reg2
            elif opCode[0] == 20: # SUBRI reg, type, value
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                self.__SetFlags(reg.value - opCode[3], reg.value_type, reg.value, opCode[3])
                reg.value -= opCode[3]
            elif opCode[0] == 23: # MULRR reg, reg
                reg1: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg2: BytecodeRegister = self.opcode_to_register_map[opCode[2]]
                self.__SetFlags(reg1.value * reg2.value, reg1.value_type, reg1.value, reg2.value)
                reg1 *= reg2
            elif opCode[0] == 22: # MULRI reg, type, value
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                self.__SetFlags(reg.value * opCode[3], reg.value_type, reg.value, opCode[3])
                reg.value *= opCode[3]
            elif opCode[0] == 25: # DIVRR reg, reg
                reg1: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg2: BytecodeRegister = self.opcode_to_register_map[opCode[2]]
                self.__SetFlags(reg1.value / reg2.value, reg1.value_type, reg1.value, reg2.value)
                reg1 /= reg2
            elif opCode[0] == 24: # DIVRI reg, type, value
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                self.__SetFlags(reg.value / opCode[3], reg.value_type, reg.value, opCode[3])
                reg.value /= opCode[3]
            elif opCode[0] == 28: # POWRR reg, reg
                reg1: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg2: BytecodeRegister = self.opcode_to_register_map[opCode[2]]
                self.__SetFlags(reg1.value ** reg2.value, reg1.value_type, reg1.value, reg2.value)
                reg1 **= reg2
            elif opCode[0] == 29: # POWRI reg, type, value
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                self.__SetFlags(reg.value ** opCode[3], reg.value_type, reg.value, opCode[3])
                reg.value **= opCode[3]
            elif opCode[0] == 27: # MODRR reg, reg
                reg1: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg2: BytecodeRegister = self.opcode_to_register_map[opCode[2]]
                self.__SetFlags(reg1.value % reg2.value, reg1.value_type, reg1.value, reg2.value)
                reg1 %= reg2
            elif opCode[0] == 26: # MODRI reg, type, value
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                self.__SetFlags(reg.value % opCode[3], reg.value_type, reg.value, opCode[3])
                reg.value %= opCode[3]
            elif opCode[0] == 31: # ANDRR reg, reg
                reg1: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg2: BytecodeRegister = self.opcode_to_register_map[opCode[2]]
                reg1.value = reg1.value is True and reg2.value is True
                self.flags.zero = reg1.value is True
            elif opCode[0] == 30: # ANDRI reg, type, value
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg.value = reg.value is True and opCode[3] is True
            elif opCode[0] == 32: # ORRI reg, type, value
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg.value = reg.value is True or opCode[3] is True
                self.flags.zero = reg.value is True
            elif opCode[0] == 8: # DJNZ addr
                self.rcx.value -= 1
                self.flags.zero = self.rcx.value == 0
                if self.rcx.value != 0:
                    self.rip.value = opCode[1]
            elif opCode[0] == 61: # CMPRTI reg, type
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                self.flags.zero = reg.value_type == opCode[2]
            elif opCode[0] == 64: # ERROR msg
                self._Error(f"{opCode[1]}, (RIP: {self.rip.value-1})")
            elif opCode[0] == 65: # ERRORZ msg
                if self.flags.zero == True:
                    self._Error(f"{opCode[1]}, (RIP: {self.rip.value-1})")
            elif opCode[0] == 66: # ERRORNZ msg
                if self.flags.zero == False:
                    self._Error(f"{opCode[1]}, (RIP: {self.rip.value-1})")
            elif opCode[0] == 51: # INC reg
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg.value += 1
            elif opCode[0] == 52: # DEC reg
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg.value -= 1
            elif opCode[0] == 53: # LEN reg
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg.value = len(reg.value)
                reg.value_type = AstNodetype.INTEGER
            elif opCode[0] == 54: # LENR reg, reg
                reg1: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg2: BytecodeRegister = self.opcode_to_register_map[opCode[2]]
                reg1.value = len(reg2.value)
                reg1.value_type = AstNodetype.INTEGER
            elif opCode[0] == 62: # SETRTI reg, type
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg.value_type = opCode[2]
            elif opCode[0] == 72: # MOVRTOA
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg.value = [reg.value]
                reg.value_type = AstNodetype.ARRAY
            elif opCode[0] == 83: # MOVATOR
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg.value = reg.value[0]
                reg.value_type = typeFromValue(reg.value)
            elif opCode[0] == 71: # HASFLDRR record has field function
                reg1: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg2: BytecodeRegister = self.opcode_to_register_map[opCode[2]]
                self.flags.zero = reg2.value in reg1.value.keys()
            elif opCode[0] == 73: # TYPE reg gets the type of the value of a register, basically puts reg.value_type in reg.value.
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg.value = reg.value_type
                reg.value_type = AstNodetype.TYPE
            # STACK, REGS, PRINTR are debugging functions, normally not used. So these should always be checked last.
            elif opCode[0] == 0: # NOP
                pass
            elif opCode[0] == 74: # STACK
                ShowStack(self.stack, self.rsp, self.rbp)
            elif opCode[0] == 75: # REGS
                ShowRegisters(rax = self.rax, rbx = self.rbx, rcx = self.rcx, rdx = self.rdx,
                              rbp = self.rbp, rsp = self.rsp, rip = self.rip, rsi = self.rsi,
                              rdi = self.rdi,  r8 = self.r8,   r9 = self.r9,  r10 = self.r10,
                              r11 = self.r11, r12 = self.r12, r13 = self.r13, r14 = self.r14,
                              r15 = self.r15, flags = self.flags)
            elif opCode[0] == 76: # PRINTR reg
                reg: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                if reg.value_type == AstNodetype.NIL:
                    print(f"{reg.name}: nil (NIL)")
                value = f"{reg.value}"
                if reg.value_type == AstNodetype.BOOLEAN:
                    value = "true" if reg.value == 1 or reg.value is True else "false"
                print(f"{reg.name} {value} ({reg.value_type.name})")
            elif opCode[0] == 77: # DATASEG metadata
                pass
            elif opCode[0] == 78: # MERGE reg1, reg2, reg3
                reg1: BytecodeRegister = self.opcode_to_register_map[opCode[1]]
                reg2: BytecodeRegister = self.opcode_to_register_map[opCode[2]]
                reg3: BytecodeRegister = self.opcode_to_register_map[opCode[3]]
                if reg2.value_type == AstNodetype.RECORD:
                    reg2.value = [reg2.value]
                    reg2.value_type = AstNodetype.ARRAY
                if reg3.value_type == AstNodetype.RECORD:
                    reg3.value = [reg3.value]
                    reg3.value_type = AstNodetype.ARRAY
                # just a single record in eachwith the same set of fields, then merge them.
                if len(reg2.value) == 1 and len(reg3.value) == 1 and set(reg2.value[0].keys()) == set(reg3.value[0].keys()):
                    reg1.value = [reg2.value[0], reg3.value[0]]
                # just a single record in each, but with different fields, then merge them but also the fields,
                # overwriting any existing in the source (reg2).
                elif len(reg2.value) == 1 and len(reg3.value) == 1:
                    keys = set().union(reg2.value[0].keys(), reg3.value[0].keys())
                    reg1.value = [{k: reg2.value[0].get(k, reg3.value[0].get(k, None)) for k in keys}]
                # multiple records in each, with the same set of fields, then just append them both.
                elif set(reg2.value[0].keys()) == set(reg3.value[0].keys()):
                    reg1.value = reg2.value.copy()
                    reg1.value.extend(reg3.value)
                # multiple records in each, but with the or different fields, then merge the records and fields.
                else:
                    keys = set().union(*(d.keys() for d in reg2.value + reg3.value))
                    reg1.value = [{k: d.get(k, None) for k in keys} for d in reg2.value + reg3.value]
                reg1.value_type = AstNodetype.ARRAY
            elif opCode[0] == 79: # JMP R
                self.rip.value = self.opcode_to_register_map[opCode[1]].value
            elif opCode[0] == 80: # RESERVE size
                self.rsp.value += opCode[1]
                while len(self.stack) < self.rsp.value:
                    self.stack.append((AstNodetype.NIL, AstNodetype.NIL))
                for var in self.scope.variables:
                    if var.stack_offset < len(self.stack):
                        self.stack[var.stack_offset] = (var.node_type, var.value)
            elif opCode[0] == 81: # RESERVEDS metadata
                pass
            elif opCode[0] == 84: # DEBUGSTR string
                print(opCode[1])
            elif opCode[0] == 85: # MOVSR reg
                reg = self.opcode_to_register_map[opCode[1]]
                reg.value_type, reg.value = self.stack[self.rsp.value-1]
            else: break
            if self.flags.trap is True:
                self.Halted = True
                return -1



    def import_module(self, module_name: str) -> Optional[Any]:
        try:
            return importlib.import_module(module_name)
        except ImportError:
            return None



    def import_module_from_path(self, module_name: str) -> Optional[Any]:
        try:
            for path in SearchPath:
                path = os.path.join(path, f"{module_name}.py")
                if not os.path.exists(path): continue
                spec = importlib.util.spec_from_file_location(module_name, path)
                if spec is None: continue
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                return module
        except ImportError as ex:
            self._Error(f"Import error: {ex}")
        return None



    def run_external_function(self, module_name: str, function_name: str, param_count: int) -> Any:
        module = self.LoadedModules.get(module_name, None)
        if module is None:
            imported_module = self.import_module(module_name)
            if imported_module is None:
                imported_module = self.import_module_from_path(module_name)
                if imported_module is None:
                    self._Error(f"Module {module_name} not found.")
            module = ModuleInfo(module_name, imported_module)
            self.LoadedModules[module_name] = module
        function = module.functions.get(function_name, None)
        if function is None:
            self._Error(f"Function {function_name} not found in module {module_name}.")
        args = []
        # need to recalc stack_offset because it's possible for a params parameter to exist, and this can have many values.
        arg_count = self.stack[self.rbp.value - 4][1] # get the number of arguments from the stack.
        stack_offset = self.rbp.value - 4 - arg_count
        args = [self.stack[stack_offset+i][1] for i in range(arg_count)]
        return function(*args)
        
