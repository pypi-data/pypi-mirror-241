#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#

# This is the bytecode label object

from __future__ import annotations
from .conversion import convertToHexAddr

class BytecodeLabel:
    def __init__(self, label: int, address: int, name: str) -> BytecodeLabel:
        self.label: int = label
        self.address: int = address
        self.name: str = name

    def __str__(self) -> str:
        return f"BytecodeLabel(label={self.label}, address={convertToHexAddr(self.address)} name={self.name})"

    def __repr__(self) -> str:
        return self.__str__()
