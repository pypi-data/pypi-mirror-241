#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#

# This provides the mapping between the bytecode instructions and the mnenomics.
# The mnenomics are in x64 intel notation, that means you first get the destination
# followed by what will be assigned to the destination.
# For programmers this style is intuitive.

#* stack and memory are different places, so we handle certain instructions in special ways.
# Memory is a a Python list that holds tuples of instructions.
# Stack is also a Python list of tuples, but these are type/value pairs.

# The 'CPU' of our VM has the following registers:
# RAX, RBX, RCX, RDS, RSI, RDI, RSP, RBP,
#  R8,  R9,  R10, R11, R12, R13, R14, R15
# RIP, FLAGS

# The stack pointer is RSP.
# The base pointer is RBP.
# The instruction pointer is RIP.
# The flags register is FLAGS.

# The stack pointer is used to point to the top of the stack.
# The base pointer is used to point to the bottom of the stack for a given scope.
# The instruction pointer is used to point to the instruction that is going to be executed,
# it is updated once every execution step.
# The flags register is used to store the flags:
# The flags register in a CPU is used to store the status of the processor after an operation.
# In a Python application representing a virtual CPU,
# the flags register is used to store the status of the processor after an operation.
# The following are the flags and their meanings:
# - **Carry flag (CF)**: Set when there is an overflow from the most significant bit (MSB) of the result. This flag is used to detect unsigned arithmetic overflow.
# - **Zero flag (ZF)**: Set when the result of an operation is zero.
# - **Sign flag (SF)**: Set when the result of an operation is negative.
# - **Overflow flag (OF)**: Set when there is an overflow from the sign bit of the result. This flag is used to detect signed arithmetic overflow.
# - **Direction flag (DF)**: Determines whether string operations increment or decrement their pointers.
# - **Interrupt flag (IF)**: Determines whether interrupts are enabled or disabled.
# - **Trap flag (TF)**: Determines whether single-step debugging is enabled or disabled.
# - **Supervisor flag (SF)**: Determines whether the processor is running in user mode or supervisor mode.
# - **Negative flag (NF)**: Set when the result of an operation has its most significant bit set.

# NOTE: While the individual flags are set or cleared based on the result of an operation,
# the actual value of the flags register itself is not changed.
# so vm.flags.value is always 0, but vm.flags.zero can be True of False.

# NOTE: While the flags register has many flags, only the states for the ZF and CF are maintained.
# The reason for this is plain and simple performance.
# It is very expensive to keep the state of flags, especially the bit state in the register itself.


from typing import Dict, List, Optional

class MacalInstruction:
    def __init__(self,
                 name: str,
                 opcode: int,
                 operands: Optional[List[str]] = None,
                 description: Optional[str] = None):
        self.Name: str = name
        self.Opcode: int = opcode
        self.Operands: List[str] = [] if operands is None else operands
        self.Description: str = "" if description is None else description

    def __str__(self) -> str:
        return f"{self.Name} {', '.join(self.Operands)}"

    def __repr__(self) -> str:
        return self.__str__()

class MacalInstructionList:
    def __init__(self):
        self.instructions: Dict[int, MacalInstruction] = {}
        self.named_instructions: Dict[str, MacalInstruction] = {}
        # These are the instructions that are implemented in the VM.
        self.add("NOP",      [],                "no operation")
        self.add("JMP",      ["addr"],          "jump to addr")
        self.add("JMPZ",     ["addr"],          "jump to addr if zero flag set")
        self.add("JMPNZ",    ["addr"],          "jump to addr if zero flag not set")
        self.add("JMPLT",    ["addr"],          "jump to addr if less than flag set")
        self.add("JMPGT",    ["addr"],          "jump to addr if greater than flag set")
        self.add("JMPLTE",   ["addr"],          "jump to addr if less than or equal flag set")
        self.add("JMPGTE",   ["addr"],          "jump to addr if greater than or equal flag set")
        self.add("DJNZ",     ["addr"],          "decrement rcx, jump to addr if not zero for loops.")
        self.add("PUSH",     ["reg"],           "put register on stack")
        self.add("POP",      ["reg"],           "get register from stack")
        self.add("MOVRR",    ["reg1", "reg2"],  "reg1 = reg2")
        self.add("MOVRI",    ["reg", "imm"],    "reg  = imm")
        self.add("MOVMI",    ["[addr]", "imm"], "sets the value at addr to imm")
        self.add("MOVRM",    ["reg", "[addr]"], "reg  = value at addr")
        self.add("MOVMR",    ["[addr]", "reg"], "value at addr = reg")
        self.add("CMPRI",    ["reg", "imm"],    "compare value of reg to imm, sets ZF, SF, CF, OF")
        self.add("CMPRR",    ["reg1", "reg2"],  "compare value of reg1 to reg2, sets ZF, SF, CF, OF")
        self.add("ADDRI",    ["reg", "imm"],    "add imm to reg")
        self.add("ADDRR",    ["reg1", "reg2"],  "add reg2 to reg1")
        self.add("SUBRI",    ["reg", "imm"],    "subtract imm from reg")
        self.add("SUBRR",    ["reg1", "reg2"],  "subtract reg2 from reg1")
        self.add("MULRI",    ["reg", "imm"],    "multiply reg by imm")
        self.add("MULRR",    ["reg1", "reg2"],  "multiply reg1 by reg2")
        self.add("DIVRI",    ["reg", "imm"],    "divide reg by imm")
        self.add("DIVRR",    ["reg1", "reg2"],  "divide reg1 by reg2")
        self.add("MODRI",    ["reg", "imm"],    "modulus reg by imm")
        self.add("MODRR",    ["reg1", "reg2"],  "modulus reg1 by reg2")
        self.add("POWRR",    ["reg1", "reg2"],  "reg1 = reg1 ^ reg2")
        self.add("POWRI",    ["reg", "imm"],    "reg = reg ^ imm")
        self.add("ANDRI",    ["reg", "imm"],    "and reg by imm")
        self.add("ANDRR",    ["reg1", "reg2"],  "and reg1 by reg2")
        self.add("ORRI",     ["reg", "imm"],    "or reg by imm")
        self.add("ORRR",     ["reg1", "reg2"],  "or reg1 by reg2")
        self.add("XORI",     ["reg", "imm"],    "xor reg by imm")
        self.add("XOR",      ["reg1", "reg2"],  "xor reg1 by reg2, sets ZF if result is zero")
        self.add("NEG",      ["reg"],           "negate reg")
        self.add("NOT",      ["reg"],           "not reg")
        self.add("SETZR",    ["reg"],           "set reg.value = 1 if ZF = 1")
        self.add("SETNZR",   ["reg"],           "set reg.value = 1 if ZF = 0")
        self.add("SETLR",    ["reg"],           "set reg.value = 1 if CF = 1 and ZF = 0")
        self.add("SETGR",    ["reg"],           "set reg.value = 1 if CF = 0 and ZF = 0")
        self.add("SETLER",   ["reg"],           "set reg.value = 1 if CF = 1 or ZF = 1")
        self.add("SETGER",   ["reg"],           "set reg.value = 1 if CF = 0 or ZF = 1")
        self.add("CALL",     ["addr"],          "call function at addr")
        self.add("CALLR",    ["reg"],           "call function at reg")
        self.add("CALLE",    ["module", "function", "paramcount"], "call function in external module.")
        self.add("RET",      [],                "return from function")
        self.add("RETZ",     [],                "return from function if zero flag set")
        self.add("RETNZ",    [],                "return from function if zero flag not set")
        self.add("HALT",     [],                "halt execution")
        self.add("INC",      ["reg"],           "reg = reg + 1")
        self.add("DEC",      ["reg"],           "reg = reg - 1")
        self.add("LEN",      ["reg"],           "reg = len(reg)")
        self.add("LENR",     ["reg1", "reg2"],  "reg1 = len(reg2)")
        self.add("INKEYS",   ["reg1", "reg2"],  "reg1 = reg1 in reg2.keys()")
        self.add("LOAD",     ["reg", "offset"], "Loads a variable from stack offset into reg")
        self.add("STOR",     ["offset", "reg"], "Stores a variable from reg into stack offset")
        self.add("LOADR",    ["reg", "reg", "offset"], "Loads a variable from stack offset relative to rbp into reg")
        self.add("STORR",    ["reg", "offset", "reg"], "Stores a variable from reg into stack offset, offset is relative to rbp")
        self.add("STORIR",   ["reg1", "reg2"],  "Stores a variable from reg2 into stack at the offset in reg1")
        self.add("CMPRTI",   ["reg", "type"],    "compare value type information of reg to imm, sets ZF, SF, CF, OF")
        self.add("SETRTI" ,  ["reg", "type"],    "set reg.type = imm")
        self.add("APPEND" ,  ["reg1", "reg2"],  "append reg1[] = reg2")
        self.add("ERROR",    ["errmsg"],        "print errmsg and halt")
        self.add("ERRORZ",   ["errmsg"],        "if zero flag set, print errmsg and halt")
        self.add("ERRORNZ",  ["errmsg"],        "if zero flag is not set, print errmsg and halt")
        self.add("PRNT",     [],                "print rax")
        self.add("INDEX",    [],                "rax = rax[rbx]")
        self.add("FEINDEX",  [],                "rax = rax[rbx] with the special note that rbx is the index to the keys() of a record if rax is a record, otherwise just like INDEX")
        self.add("INDEXR",   ["reg"],           "rax[rbx] = reg")
        self.add("HASFLDRR", ["reg1", "reg2"],  "reg1 = reg1.has_field(reg2)")
        self.add("MOVRTOA",  ["reg"],           "reg = [reg], the record in reg is moved into an array with that record as an element.")
        self.add("TYPE",     ["reg"],           "reg = type(reg)")
        # These instructions are for debugging purposes only.
        self.add("STACK",    [],                "show stack for debugging")
        self.add("REGS",     [],                "show registers for debugging")
        self.add("PRNTR",    ["reg"],           "print reg, debug printing register name, value, type")
        self.add("DATASEG",  ["metadata"],      "set metadata for debugging")
        self.add("MERGE",    ["reg1", "reg2", "reg3"],  "merge reg2 and reg3 into reg1 reg1 = [reg2] + [reg3]")
        self.add("JMPR",     ["reg"],           "jump to reg")
        self.add("RESERVE",  ["imm"],           "reserve imm entries on the stack")
        self.add("RESERVEDS", ["metadata"],     "datasegment with metadata for variables that are reserved on the stack")
        self.add("LOADIR",   ["reg1", "reg2"],  "reg1 = stack[reg2]")
        self.add("MOVATOR",  ["reg"],           "reg = reg[0], the first record in the array in reg is moved into reg.")

    def add(self, name: str, operands: Optional[List[str]] = None, description: Optional[str] = None):
        opcode = len(self.instructions)
        instruction = MacalInstruction(name, opcode, operands, description)
        self.instructions[opcode] = instruction
        self.named_instructions[name] = instruction

    def get(self, opcode: int) -> MacalInstruction:
        if opcode not in self.instructions:
            raise ValueError(f"Unknown opcode {opcode}")
        return self.instructions[opcode]

    def getByName(self, name: str) -> MacalInstruction:
        if name not in self.named_instructions:
            raise ValueError(f"Unknown instruction {name}")
        return self.named_instructions[name]

    def __getitem__(self, opcode: int) -> MacalInstruction:
        return self.get(opcode)

    def __getattr__(self, name: str) -> int:
        return self.getByName(name).Opcode

    def __len__(self) -> int:
        return len(self.instructions)

    def __iter__(self):
        return iter(self.instructions.values())

    def __str__(self) -> str:
        return "\n".join([str(instruction) for instruction in self.named_instructions.values()])

    def __repr__(self) -> str:
        return self.__str__()

    def fromOpcode(self, opcode: int) -> MacalInstruction:
        return self.get(opcode)

Opcode = MacalInstructionList()