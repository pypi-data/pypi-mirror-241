#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#

# This is the runtime scope for the Macal virtual machine
#
# The primary function of this class is to provide a scope for the Macal virtual machine.
# It is used to store the values of the pre-defined variables, if there are any.

from __future__ import annotations

from typing import Any, List, Optional, Tuple

from .ast_nodetype import AstNodetype
from .ct_variable import CTVariable
from .macal_conversions import typeFromValue


class RuntimeScope:
    def __init__(self) -> RuntimeScope:
        self.name: str = "runtime"
        self.variables: List[CTVariable] = []

    def DefineVariable(self, name: str, stack_offset: int) -> CTVariable:
        var = CTVariable(name, self)
        var.stack_offset = stack_offset
        self.variables.append(var)
        return var

    def GetVariable(self, name: str) -> Optional[CTVariable]:
        return next((var for var in self.variables if var.name == name), None)

    def SetVariable(self, name: str, value: Any) -> None:
        var = self.GetVariable(name)
        if var is None:
            raise Exception(f"Runtime Error: Variable {name} does not exist.")
        var.value = value
        var.node_type = typeFromValue(value)
