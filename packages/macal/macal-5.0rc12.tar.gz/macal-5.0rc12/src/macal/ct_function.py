#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#

# This is the compile time function information.

from __future__ import annotations
from typing import List
from .conversion import convertToHexAddr
from .ast_node_function_parameter import AstNodeFunctionParameter

class CTFunction:
    def __init__(self, start_address: int, name: str) -> CTFunction:
        self.start_address: int = start_address
        self.name: str = name
        self.return_type: str = ""
        self.external: bool = False
        self.module: str = ''
        self.function: str = ''
        self.parameters: List[AstNodeFunctionParameter] = []

    def __str__(self) -> str:
        return f"CTFunction({convertToHexAddr(self.start_address)}, {self.name})"

    def __repr__(self) -> str:
        return self.__str__()

class CTFunctionCall:
    def __init__(self, name: str, from_addr: int, to_addr) -> CTFunctionCall:
        self.name: str = name
        self.from_addr: int = from_addr
        self.to_addr: int = to_addr

    def __str__(self) -> str:
        return f"CTFunctionCall({self.name}, {convertToHexAddr(self.from_addr)} -> {convertToHexAddr(self.to_addr)})"

    def __repr__(self) -> str:
        return self.__str__()
