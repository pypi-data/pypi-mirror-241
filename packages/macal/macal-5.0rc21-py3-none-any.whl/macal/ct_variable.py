#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#

# Compile time variable

from __future__ import annotations
from typing import Any, List
from .ast_nodetype import AstNodetype
from .ast_node_expression import AstNodeExpression

class CTVariable:
    # scope is a CompilerScope, but unfortunately we can't import it here because of circular imports.
    def __init__(self, name: str, scope) -> CTVariable:
        self.name: str = name
        self.node_type: AstNodetype = AstNodetype.NIL
        self.value: Any = None
        self.stack_offset: int = 0
        self.index: List[AstNodeExpression] = []
        self.scope = scope
        self.const = False

    def __str__(self) -> str:
        return f"CTVariable({self.name}, {self.node_type}, {self.value}, {self.stack_offset})"

    def __repr__(self) -> str:
        return self.__str__()


