#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#

# Compiler scope is used to keep track of certain things that are needed during compilation.

from __future__ import annotations
from typing import Dict, List, Optional, Union
from .bytecode_label import BytecodeLabel
from .bytecode_jump import BytecodeJump
from .ct_function import CTFunction
from .ct_variable import CTVariable
from .switch_case_table import SwitchCaseTable

class FunctionAlias:
    def __init__(self, alias: str, name: str) -> FunctionAlias:
        self.alias: str = alias
        self.name: str = name

class CompilerScope:
    def __init__(self, name: str, parent: CompilerScope) -> CompilerScope:
        self.name: str = name
        self.parent: CompilerScope = parent
        # symbol table
        self.functions: List[CTFunction] = []
        self._libraries: Dict[str, int] = {}
        self.variables: List[CTVariable] = []
        self.function_aliasses: List[FunctionAlias] = []

        self.labels: List[BytecodeLabel] = []
        self.jump_table: List[BytecodeJump] = []
        self.switch_jump_tables: List[SwitchCaseTable] = []

        self.can_search_parent: bool = True
        self.children: List[CompilerScope] = []

        self.continue_label: Optional[int] = None
        self.break_label: Optional[int] = None
        self._main_label_name = 'main'
        self.exit_label: Optional[int] = None # set by compiler in function definition compilate.
        self.rbp_offset: int = 0 # set by compiler in scope creation.
        self.is_function_definition = False

    @property
    def root(self) -> CompilerScope:
        if self.parent is None:
            return self
        return self.parent.root

    @property
    def label_count(self) -> int:
        return len(self.root.labels)

    @property
    def variable_count(self) -> int:
        return len(self.variables)

    @property
    def function_count(self) -> int:
        return len(self.functions)

    @property
    def libraries(self) -> Dict[str, int]:
        return self.root._libraries

    @property
    def library_count(self) -> int:
        return len(self.root.libraries)

    @property
    def main_label_name(self) -> str:
        return self.root._main_label_name

    def new_child(self, name: str, base_pointer) -> CompilerScope:
        name = f'{self.name}.{name}_{len(self.children)}'
        child = CompilerScope(name, self)
        child.rbp_offset = base_pointer
        self.children.append(child)
        return child

    def remove_child(self, child: CompilerScope) -> None:
        self.children.remove(child)

    def get_new_label(self, name: Optional[str] = None) -> Optional[int]:
        id = len(self.root.labels)
        if name is None:
            name = f'label'
        lbl_name = f'{name}_{id}' # ensure unique label name
        if name == "main":
            self.root._main_label_name = lbl_name
        #if any(label.name == lbl_name for label in self.root.labels):
        #    return None
        self.root.labels.append(BytecodeLabel(id, -1, lbl_name))
        return id

    def get_label(self, name: str) -> Optional[int]:
        return next((label.id for label in self.root.labels if label.name == name), None)

    def set_label_address(self, id: int, address: int) -> bool:
        if not isinstance(address, int):
            raise TypeError(f"address must be an int, not {type(address)}")
        if id < 0 or id >= len(self.root.labels):
            return False
        self.root.labels[id].address = address
        return True

    def new_jump(self, address: int, label_id: int) -> bool:
        self.root.jump_table.append(BytecodeJump(address, label_id))
        return True

    def define_variable(self, name: str, offset: int) -> Optional[CTVariable]:
        var = CTVariable(name, self)
        var.stack_offset = offset
        self.variables.append(var)
        return var

    def get_variable(self, name: str) -> Optional[Union[CTVariable, CTFunction]]:
        var = next((var for var in self.variables if var.name == name), None)
        if var is not None:
            return var
        if self.parent is not None and self.can_search_parent:
            var = self.parent.get_variable(name)
            if var is not None:
                return var
        funcname = f"{self.name}.{name}"
        func = next((func for func in self.functions if func.name == funcname), None)
        return func

    def find_variable(self, name: str) -> Optional[CTVariable]:
        var = next((var for var in self.variables if var.name == name), None)
        if var is not None: return var
        if self.parent is not None and self.can_search_parent:
            return self.parent.find_variable(name)
        return None

    def define_function(self, name: str, function_start_address: int) -> Optional[CTFunction]:
        if any(func.name == name for func in self.functions):
            return None
        func = CTFunction(function_start_address, name)
        self.functions.append(func)
        return func

    def define_function_alias(self, var_name: str, func_name: str) -> None:
        if any(alias.alias == var_name for alias in self.function_aliasses):
            return None
        self.function_aliasses.append(FunctionAlias(var_name, func_name))

    def get_function_alias(self, var_name: str) -> Optional[str]:
        alias = next((alias for alias in self.function_aliasses if alias.alias == var_name), None)
        if alias is None and self.parent is not None:
            alias = self.parent.get_function_alias(var_name)
        return alias

    def get_function_by_alias(self, alias: str) -> Optional[CTFunction]:
        alias = self.get_function_alias(alias)
        if alias is None:
            return None
        return self.get_function(alias.name)

    # need to give this another name if we keep the latter.
    def get_function(self, name: str) -> Optional[CTFunction]:
        func = next((func for func in self.functions if func.name == name), None)
        if func is None and self.parent is not None:
            func = self.parent.get_function(name)
        return func

    def get_function_by_address(self, address: int) -> Optional[CTFunction]:
        func = next((func for func in self.functions if func.start_address == address), None)
        if func is None and self.parent is not None:
            func = self.parent.get_function_by_address(address)
        return func

    def define_library(self, name: str) -> Optional[int]:
        if name in self.root._libraries:
            return None
        id = len(self.root._libraries)
        self.root._libraries[name] = id
        return id

    def get_library(self, name: str) -> Optional[int]:
        if name in self.root._libraries:
            return self.root._libraries[name]
        return None

    def __str__(self) -> str:
        return f"CompilerScope({self.name})"

    def __repr__(self) -> str:
        return self.__str__()

    def discard(self) -> None:
        if self.parent != None:
            self.parent.remove_child(self)