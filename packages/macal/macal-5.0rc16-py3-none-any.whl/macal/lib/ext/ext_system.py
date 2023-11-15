# Product:   Macal 2
# Author:    Marco Caspers
# Date:      16-10-2023
#

"""Macal system library implementation"""

from typing import Any
import platform
import os
import sys

def Console(*args, **kwargs):
    print(*args, **kwargs)


def Array(*args) -> None:
    arr = []
    for arg in args:
        arr.append(arg)
    return arr
    

def RecordHasField(record: dict, fieldname: str) -> bool:
    return fieldname in record

def GetPlatform() -> None:
    return platform.system()

def RecordItems(var : dict) -> list:
    """Implementation of Items function used in conjunction with foreach for iterating over records.  Items returns key/value pairs."""
    return [{key: value} for key, value in var.items()]

def RecordItemKey(var : dict) -> str:
    """Implementation of Key function used in conjunction the Items function that returns key/value pairs. Key returns the key part of a key value pair."""
    for k, _ in var.items(): #there are different ways, but this is by far the most simple and safe way to do it.
        return k

def RecordKeys(var: dict) -> list:
    """Implementation of Keys function used in conjunction the Items function that returns key/value pairs. Key returns the key part of a key value pair."""
    return [k for k in var.keys()]

def RecordItemValue(var: dict) -> Any:
    """Implementation of Value function used in conjunction the Items function that returns key/value pairs. Value returns the value part of a key value pair."""
    for _, v in var.items(): #there are different ways, but this is by far the most simple and safe way to do it.
        return v

def RecordValues(var: dict) -> list:
    """Implementation of Value function used in conjunction the Items function that returns key/value pairs. Value returns the value part of a key value pair."""
    return [v for v in var.values()]

def GetEnv(varname: str) -> str:
    """Returns the value of an environment variable"""
    return os.getenv(varname)

def SetEnv(varname: str, value: str) -> None:
    """Sets the value of an environment variable"""
    os.environ[varname] = value

def GetArgs() -> list:
    """Returns a list of arguments passed to the program"""
    return sys.argv

def GetArg(index: int) -> str:
    """Returns a single argument passed to the program"""
    return sys.argv[index]

def GetArgCount() -> int:
    """Returns the number of arguments passed to the program"""
    return len(sys.argv)