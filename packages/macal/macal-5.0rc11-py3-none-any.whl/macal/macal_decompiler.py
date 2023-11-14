#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#

# Decompiler for Macal VM instructionset.

from __future__ import annotations
from .macal_instructions import MacalInstructionList, MacalInstruction
from .conversion import convertToHexAddr
import pyximport; pyximport.install()
from .cmacal_vm import MacalVm
from .ast_nodetype import AstNodetype

class MacalDecompiler:
    def __init__(self, filename: str, verbose: bool = False) -> MacalDecompiler:
        self.vm: MacalVm = MacalVm(filename)
        self.vm.rip.value = 0
        self.instructions: MacalInstructionList = MacalInstructionList()
        self.metadata: dict = {}
        self.labels: list = []
        self.verbose: bool = verbose
        if filename is not None:
            data = self.vm.memory[len(self.vm.memory)-1]
            if data[0] == 77:
                self.metadata = data[1]
                self.labels = self.metadata['LABELS']



    def __PrintLabels(self, addr: int) -> None:
        flag = False
        for label in self.labels:
            if label[1] == addr:
                print(f"{label[0]}:", end=' ')
                flag = True
        if flag is True:
            print()



    def Decompile(self):
        addr = 0
        print()
        print(f"Decompiling: {self.vm.filename}")
        print()
        print("Address       Instruction")
        while addr < len(self.vm.memory):
            self.__PrintLabels(addr)
            opcode = self.vm.memory[addr]
            op: MacalInstruction = self.instructions.fromOpcode(opcode[0])
            print(f"{convertToHexAddr(addr)}    {op.Name:<6} ", end=' ')
            n = 1
            for operand in op.Operands:
                if n > 1:
                    print(", ", end='')
                if operand == "addr":
                    print(convertToHexAddr(opcode[n]), end='')
                elif operand == "[addr]":
                    print(f"[{convertToHexAddr(opcode[n])}]", end='')
                elif operand.startswith("reg"):
                    print(f"{self.vm.opcode_to_register_map[opcode[n]].name}", end='')
                elif operand == "imm":
                    value = f"{opcode[n+1]}"
                    if opcode[n] == AstNodetype.STRING:
                        value = value.replace('\n', '\\n')	# escape newlines
                        value = value.replace('\r', '\\r')	# escape cr
                        value = f'"{value}"'
                    print(f"{opcode[n].name} {value.strip()}", end='')
                    n += 1
                elif operand == "errmsg" or operand == "module" or operand == "function" or operand == "paramcount" or operand == "offset":
                    print(opcode[n], end='')
                elif operand == "metadata":
                    print("METADATA", end='')
                elif operand == "type":
                    print(opcode[n].name, end='')
                else:
                    raise Exception(f"Unknown operand: {operand}")
                n+= 1
            print()
            addr += 1
        print()
        print(f"Finished decompiling: {self.vm.filename}")
        print()

