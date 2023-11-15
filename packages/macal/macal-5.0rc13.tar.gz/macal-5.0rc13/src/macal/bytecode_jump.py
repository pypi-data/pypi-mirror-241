#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#

# This is the information for a bytecode jump instruction.

from __future__ import annotations
from .conversion import convertToHexAddr

class BytecodeJump:
    def __init__(self, address: int, label: int) -> BytecodeJump:
        self.address: int = address
        self.label: int = label

    def __str__(self) -> str:
        return f"BytecodeJump(address={convertToHexAddr(self.address)}, label={self.label})"

    def __repr__(self) -> str:
        return self.__str__()