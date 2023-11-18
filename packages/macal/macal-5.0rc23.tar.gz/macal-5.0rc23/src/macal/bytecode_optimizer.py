#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#

# This is the bytecode optimizer.
# The Optimizer will attempt to optimize the bytecode that was emitted by the compiler by the following strategies:
# - remove push/pop pairs for the same register.

from __future__ import annotations

from .bytecode_address import Address
from .compiler_scope import CompilerScope
from .macal_instructions import MacalInstructionList

import pyximport; pyximport.install()
from .cmacal_vm import MacalVm


class BytecodeOptimizer:
    def __init__(self, vm: MacalVm, scope: CompilerScope):
        self.vm = vm
        self.scope = scope
        self.result = MacalVm()
        self.instructions = MacalInstructionList()

    def fix_jumps_for_push_pop_removal(addr):
        pass

    def get_label(self, lbl):
        for label in self.scope.labels:
            if label.label == lbl:
                return label

    def process(self):
        addr = 9
        pairs = 0
        jmp = 0
        fix = 0
        while addr < self.vm.rip.value:
            start = addr
            opcode = self.vm.memory._memory[addr]
            op = self.instructions.instructions[opcode]
            #  9 = PUSH
            # 10 = POP
            if (
                opcode == 9
                and self.vm.memory._memory[addr + 2] == 10
                and self.vm.memory._memory[addr + 1] == self.vm.memory._memory[addr + 3]
            ):
                pairs += 1
            if op.Name == "JMP":
                jmp += 1
                for jump in self.scope.jump_table:
                    if jump.address == addr:
                        lbl = self.get_label(jump.label)
                        print(f"jump: {addr} {jump.address} -> {jump.label} {lbl.address}, {lbl.name}")
                        if lbl.address == addr + 9:
                            print("---------------------------> FOUND one")
                            fix += 1
                        next = self.vm.memory._memory[lbl.address]
                        nxtop = self.instructions.instructions[next]
                        if nxtop.Name == "JMP":
                            print("----------> FOUND JUMP TO JUMP")
            print(op.Name, ", ".join(op.Operands))
            if op.Length == -1:
                str = self.vm.peek_string(Address(addr + 1))
                addr += len(str)
                addr += 2  # opcode + zero terminator for the string.
            elif op.Name == "CALLE":
                addr += 9  # op + param count.
                str = self.vm.peek_string(Address(addr))
                addr += len(str)
                addr += 1
                str = self.vm.peek_string(Address(addr))
                addr += len(str)
                addr += 1
            elif op.Length == -3:
                # self.vm.show_memory(addr, 32)
                addr += 2  # the op and the register
                type = self.vm.opcode_to_type_map[self.vm.memory._memory[addr] - 128]
                addr += 1  # the type
                rip = Address(addr)
                value = self.vm.peek_value(rip, type)
                addr = rip.address
            else:
                addr += op.Length

        print(pairs)
        print(jmp)
        print(fix)
        import sys

        sys.exit(0)
