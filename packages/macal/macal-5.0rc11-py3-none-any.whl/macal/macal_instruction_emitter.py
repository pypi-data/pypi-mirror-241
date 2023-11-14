#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#

# Compiler helper for Macal

# write instructions to memory
# NOTE: When the instruction has no parameters, you must emit the tuple as (opcode,)
# If you do not provide the comma, pickle will deserialize it as a single integer.
# And that will fail when you try to execute it.

from __future__ import annotations
import sys
from typing import Any
from .ast_nodetype import AstNodetype
from .bytecode_register import BytecodeRegister

class MacalInstructionEmitter:
    def __init__(self, memory, rip: BytecodeRegister, rsp: BytecodeRegister, rbp: BytecodeRegister) -> MacalInstructionEmitter:
        self.memory = memory
        self.rip: BytecodeRegister = rip
        self.rsp: BytecodeRegister = rsp
        self.rbp: BytecodeRegister = rbp
        self.do_raise: bool = True # change this to false for production.


    def error(self, message: str) -> None:
        msg = f"Compiler Error: {message}"
        if self.do_raise:
            raise Exception(msg)
        print(msg)
        sys.exit(1)

    def NOP(self) -> None:
        self.memory[self.rip.value] = (0,)
        self.rip.value += 1
    
    def JMP(self, addr: int) -> None:
        self.memory[self.rip.value] = (1, addr)
        self.rip.value += 1
    
    def JMPZ(self, addr: int) -> None:
        self.memory[self.rip.value] = (2, addr)
        self.rip.value += 1
    
    def JMPNZ(self, addr: int) -> None:
        self.memory[self.rip.value] = (3, addr)
        self.rip.value += 1
    
    def JMPLT(self, addr: int) -> None:
        self.memory[self.rip.value] = (4, addr)
        self.rip.value += 1
    
    def JMPGT(self, addr: int) -> None:
        self.memory[self.rip.value] = (5, addr)
        self.rip.value += 1
    
    def JMPLTE(self, addr: int) -> None:
        self.memory[self.rip.value] = (6, addr)
        self.rip.value += 1
    
    def JMPGTE(self, addr: int) -> None:
        self.memory[self.rip.value] = (7, addr)
        self.rip.value += 1
    
    def DJNZ(self, addr: int) -> None:
        self.memory[self.rip.value] = (8, addr)
        self.rip.value += 1
    
    def PUSH(self, reg: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (9, reg.opcode)
        self.rip.value += 1
        self.rsp.value += 1
    
    def POP(self, reg: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (10, reg.opcode)
        self.rip.value += 1
        self.rsp.value -= 1
        #print(self.memory[0:self.rip.value-1])
        #sys.exit(1)
    
    def MOVRR(self, reg1: BytecodeRegister, reg2: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (11, reg1.opcode, reg2.opcode)
        self.rip.value += 1
        if reg1.name == 'RBP' and reg2.name == 'RSP':
            self.rbp.value = self.rsp.value
        elif reg1.name == 'RSP' and reg2.name == 'RBP':
            self.rsp.value = self.rbp.value
    
    def MOVRI(self, reg: BytecodeRegister, node_type: AstNodetype, value: Any) -> None:
        self.memory[self.rip.value] = (12, reg.opcode, node_type, value)
        self.rip.value += 1
    
    def MOVMI(self, addr, node_type: AstNodetype, value: Any) -> None:
        self.memory[self.rip.value] = (13, addr, node_type, value)
        self.rip.value += 1
    
    def MOVRM(self, reg: BytecodeRegister, addr) -> None:
        self.memory[self.rip.value] = (14, reg.opcode, addr)
        self.rip.value += 1
    
    def MOVMR(self, addr, reg: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (15, addr, reg.opcode)
        self.rip.value += 1
    
    def CMPRI(self, reg: BytecodeRegister, node_type: AstNodetype, value: Any) -> None:
        self.memory[self.rip.value] = (16, reg.opcode, node_type, value)
        self.rip.value += 1
    
    def CMPRR(self, reg1: BytecodeRegister, reg2: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (17, reg1.opcode, reg2.opcode)
        self.rip.value += 1
    
    def ADDRI(self, reg: BytecodeRegister, node_type: AstNodetype, value: Any) -> None:
        self.memory[self.rip.value] = (18, reg.opcode, node_type, value)
        self.rip.value += 1
    
    def ADDRR(self, reg1: BytecodeRegister, reg2: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (19, reg1.opcode, reg2.opcode)
        self.rip.value += 1
    
    def SUBRI(self, reg: BytecodeRegister, node_type: AstNodetype, value: Any) -> None:
        self.memory[self.rip.value] = (20, reg.opcode, node_type, value)
        self.rip.value += 1
    
    def SUBRR(self, reg1: BytecodeRegister, reg2: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (21, reg1.opcode, reg2.opcode)
        self.rip.value += 1
    
    def MULRI(self, reg: BytecodeRegister, node_type: AstNodetype, value: Any) -> None:
        self.memory[self.rip.value] = (22, reg.opcode, node_type, value)
        self.rip.value += 1
    
    def MULRR(self, reg1: BytecodeRegister, reg2: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (23, reg1.opcode, reg2.opcode)
        self.rip.value += 1
    
    def DIVRI(self, reg: BytecodeRegister, node_type: AstNodetype, value: Any) -> None:
        self.memory[self.rip.value] = (24, reg.opcode, node_type, value)
        self.rip.value += 1
    
    def DIVRR(self, reg1: BytecodeRegister, reg2: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (25, reg1.opcode, reg2.opcode)
        self.rip.value += 1
    
    def MODRI(self, reg: BytecodeRegister, node_type: AstNodetype, value: Any) -> None:
        self.memory[self.rip.value] = (26, reg.opcode, node_type, value)
        self.rip.value += 1
    
    def MODRR(self, reg1: BytecodeRegister, reg2: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (27, reg1.opcode, reg2.opcode)
        self.rip.value += 1
    
    def POWRR(self, reg1: BytecodeRegister, reg2: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (28, reg1.opcode, reg2.opcode)
        self.rip.value += 1
    
    def POWRI(self, reg: BytecodeRegister, node_type: AstNodetype, value: Any) -> None:
        self.memory[self.rip.value] = (29, reg.opcode, node_type, value)
        self.rip.value += 1
    
    def ANDRI(self, reg: BytecodeRegister, node_type: AstNodetype, value: Any) -> None:
        self.memory[self.rip.value] = (30, reg.opcode, node_type, value)
        self.rip.value += 1
    
    def ANDRR(self, reg1: BytecodeRegister, reg2: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (31, reg1.opcode, reg2.opcode)
        self.rip.value += 1
    
    def ORRI(self, reg: BytecodeRegister, node_type: AstNodetype, value: Any) -> None:
        self.memory[self.rip.value] = (32, reg.opcode, node_type, value)
        self.rip.value += 1
    
    def ORRR(self, reg1: BytecodeRegister, reg2: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (33, reg1.opcode, reg2.opcode)
        self.rip.value += 1
    
    def XORI(self, reg: BytecodeRegister, node_type: AstNodetype, value: Any) -> None:
        self.memory[self.rip.value] = (34, reg.opcode, node_type, value)
        self.rip.value += 1
    
    def XOR(self, reg1: BytecodeRegister, reg2: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (35, reg1.opcode, reg2.opcode)
        self.rip.value += 1
    
    def NEG(self, reg: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (36, reg.opcode)
        self.rip.value += 1
    
    def NOT(self, reg: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (37, reg.opcode)
        self.rip.value += 1
    
    def SETZR(self, reg: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (38, reg.opcode)
        self.rip.value += 1
    
    def SETNZR(self, reg: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (39, reg.opcode)
        self.rip.value += 1
    
    def SETLR(self, reg: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (40, reg.opcode)
        self.rip.value += 1
    
    def SETGR(self, reg: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (41, reg.opcode)
        self.rip.value += 1
    
    def SETLER(self, reg: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (42, reg.opcode)
        self.rip.value += 1
    
    def SETGER(self, reg: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (43, reg.opcode)
        self.rip.value += 1
    
    def CALL(self, addr: int) -> None:
        self.memory[self.rip.value] = (44, addr)
        self.rip.value += 1
        self.rsp.value += 1 # reserve space for the return value.
    
    def CALLR(self, reg: BytecodeRegister) -> None:
        if reg.name == "RAX":
            self.error("Can't use RAX in CALL/CALLR, RAX is reset to push a placeholder for the return value on the stack.")
        self.memory[self.rip.value] = (45, reg.opcode)
        self.rip.value += 1
        self.rsp.value += 1 # reserve space for the return value.
    
    def CALLE(self, module: str, function: str, param_count: int) -> None:
        self.memory[self.rip.value] = (46, module, function, param_count)
        self.rip.value += 1
        self.rsp.value += 1 # reserve space for the return value.
    
    def RET(self) -> None:
        self.memory[self.rip.value] = (47,)
        self.rip.value += 1
    
    def RETZ(self) -> None:
        self.memory[self.rip.value] = (48,)
        self.rip.value += 1
    
    def RETNZ(self) -> None:
        self.memory[self.rip.value] = (49,)
        self.rip.value += 1
    
    def HALT(self) -> None:
        self.memory[self.rip.value] = (50,)
        self.rip.value += 1
    
    def INC(self, reg: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (51, reg.opcode)
        self.rip.value += 1
    
    def DEC(self, reg: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (52, reg.opcode)
        self.rip.value += 1
    
    def LEN(self, reg: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (53, reg.opcode)
        self.rip.value += 1
    
    def LENR(self, reg1: BytecodeRegister, reg2: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (54, reg1.opcode, reg2.opcode)
        self.rip.value += 1
    
    def INKEYS(self, reg1: BytecodeRegister, reg2: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (55, reg1.opcode, reg2.opcode)
        self.rip.value += 1
    
    def LOAD(self, reg: BytecodeRegister, offset: int) -> None:
        self.memory[self.rip.value] = (56, reg.opcode, offset)
        self.rip.value += 1
    
    def STOR(self, offset: int, reg: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (57, offset, reg.opcode)
        self.rip.value += 1
    
    def LOADR(self, reg1: BytecodeRegister, reg2: BytecodeRegister, offset: int) -> None:
        self.memory[self.rip.value] = (58, reg1.opcode, reg2.opcode, offset)
        self.rip.value += 1
    
    def STORR(self, reg1: BytecodeRegister, offset: int, reg2: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (59, reg1.opcode, offset, reg2.opcode)
        self.rip.value += 1
    
    def STORIR(self, reg1: BytecodeRegister, reg2: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (60, reg1.opcode, reg2.opcode)
        self.rip.value += 1
    
    def CMPRTI(self, reg: BytecodeRegister, node_type: AstNodetype) -> None:
        self.memory[self.rip.value] = (61, reg.opcode, node_type)
        self.rip.value += 1
    
    def SETRTI(self, reg: BytecodeRegister, node_type: AstNodetype) -> None:
        self.memory[self.rip.value] = (62, reg.opcode, node_type)
        self.rip.value += 1
    
    def APPEND(self, reg1: BytecodeRegister, reg2: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (63, reg1.opcode, reg2.opcode)
        self.rip.value += 1
    
    def ERROR(self, errmsg) -> None:
        self.memory[self.rip.value] = (64, errmsg)
        self.rip.value += 1
    
    def ERRORZ(self, errmsg) -> None:
        self.memory[self.rip.value] = (65, errmsg)
        self.rip.value += 1
    
    def ERRORNZ(self, errmsg) -> None:
        self.memory[self.rip.value] = (66, errmsg)
        self.rip.value += 1
    
    def PRNT(self) -> None:
        self.memory[self.rip.value] = (67,)
        self.rip.value += 1
    
    def INDEX(self) -> None:
        self.memory[self.rip.value] = (68,)
        self.rip.value += 1
    
    def FEINDEX(self) -> None:
        self.memory[self.rip.value] = (69,)
        self.rip.value += 1
    
    def INDEXR(self, reg: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (70, reg.opcode)
        self.rip.value += 1
    
    def HASFLDRR(self, reg1: BytecodeRegister, reg2: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (71, reg1.opcode, reg2.opcode)
        self.rip.value += 1
    
    def MOVRTOA(self, reg: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (72, reg.opcode)
        self.rip.value += 1
    
    def TYPE(self, reg: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (73, reg.opcode)
        self.rip.value += 1
    
    def STACK(self) -> None:
        self.memory[self.rip.value] = (74,)
        self.rip.value += 1
    
    def REGS(self) -> None:
        self.memory[self.rip.value] = (75,)
        self.rip.value += 1
    
    def PRNTR(self, reg: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (76, reg.opcode)
        self.rip.value += 1
    
    def DATASEG(self, metadata: dict) -> None:
        self.memory[self.rip.value] = (77, metadata)
        self.rip.value += 1
    
    def MERGE(self, reg1: BytecodeRegister, reg2: BytecodeRegister, reg3: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (78, reg1.opcode, reg2.opcode, reg3.opcode)
        self.rip.value += 1
    
    def JMPR(self, reg: BytecodeRegister) -> None:
        self.memory[self.rip.value] = (79, reg.opcode)
        self.rip.value += 1
    
    def RESERVE(self, size: int) -> None:
        self.memory[self.rip.value] = (80, size)
        self.rip.value += 1
    
    def RESERVEDS(self, metadata: dict) -> None:
        self.memory[self.rip.value] = (81, metadata)
        self.rip.value += 1
    
    def LOADIR(self, reg1: BytecodeRegister, reg2: BytecodeRegister):
        self.memory[self.rip.value] = (82, reg1.opcode, reg2.opcode)
        self.rip.value += 1

    def MOVATOR(self, reg: BytecodeRegister):
        self.memory[self.rip.value] = (83, reg.opcode)
        self.rip.value += 1
