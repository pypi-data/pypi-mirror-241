#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#

# this is the bytecode library for the compiler and the scope.

from __future__ import annotations
from .conversion import convertToHexAddr

class BytecodeLibrary:
    def __init__(self, name: str, address: int) -> BytecodeLibrary:
        self.name: str = name
        self.address: int = address

    def __str__(self) -> str:
        return f"BytecodeLibrary(name={self.name}, address={convertToHexAddr(self.address)})"

    def __repr__(self) -> str:
        return self.__str__()