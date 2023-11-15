# Product:   Macal 2
# Author:    Marco Caspers
# Date:      16-10-2023
#
# String functions library

from typing import Any
from unidecode import unidecode

def StrLen(arg: str) -> int:
    """Implementation of len function"""
    return len(arg)

def StrLeft(arg: str, length: int) -> str:
    """Implementation of left function"""
    return arg[0:length]


def StrMid(arg: str, offset: int, length: int) ->str:
    """Implementation of mid function"""
    return arg[offset:(offset+length)]
    
def ToString(arg: Any) -> str:
    """Implementation of toString function"""
    return str(arg)        

def StrContains(needle: str, haystack: str) -> bool:
    """Implementation of strContains function"""
    return needle in haystack

def StrReplace(var: str, frm: str, wth: str) -> str:
    """Implementation of strReplace function"""
    return var.replace(frm, wth)


def StartsWith(haystack: str, needle: str) -> bool:
    """Implementation of StartsWith function"""
    return haystack.startswith(needle)

def RemoveNonAscii(text: str) -> str:
    """Implementation of RemoveNonAscii function"""
    result = unidecode(text)

def ReplaceEx(var: str, repl: Any, by: str) -> str:
    """Implementation of ReplaceEx function"""
    result = var
    for ch in repl:
        result = result.replace(ch, by)
    return result

def PadLeft(string: str, char: str, amount: int) -> Any:
    """Implementation of PadLeft function"""
    # this is counter intuitive, but the *just functions in python pad the character on the other 
    # end as what their name would imply.
    return string.rjust(amount, char)

def PadRight(string: str, char: str, amount: int) -> Any:
    """Implementation of PadRight function"""
    # this is counter intuitive, but the *just functions in python pad the character on the other 
    # end as what their name would imply.
    return string.ljust(amount, char)
    
def PadCenter(string: str, char: str, amount: int) -> Any:
    """Implementation of PadCenter function"""
    return string.center(amount, char)