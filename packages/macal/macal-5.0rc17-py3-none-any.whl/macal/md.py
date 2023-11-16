#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#

# This is the Macal decompiler, it will decompile a .mbc file into bytecode mnenomics.

import os
import argparse
from typing import Optional
from macal.__about__ import __version__, __author__, __author_email__, __license__
from macal.config import SearchPath
from macal.macal_decompiler import MacalDecompiler

bytecode_extension  = '.mbc'

def SetupSearchPath() -> None:
    search_path = [os.path.dirname(__file__),
        os.path.join(os.path.dirname(__file__), "lib"),
        os.path.join(os.path.dirname(__file__), "lib", "ext"),
        os.getcwd(),
        os.path.join(os.getcwd(), "lib"),
        os.path.join(os.getcwd(), "lib", "ext")]
    for path in search_path:
        if path not in SearchPath:
            SearchPath.append(path)

def check_file(file) -> Optional[str]:
    if file is None: return
    if not file.endswith(bytecode_extension):
        if os.path.exists(f"{file}{bytecode_extension}"):
            file = f"{file}{bytecode_extension}"
        else:
            raise Exception("Invalid Macal bytecode file.")
    return file

def BuildArgParser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Macal decompiler')
    parser.add_argument('file', nargs='?', type=check_file, help='Macal file')
    parser.add_argument('-s', '--verbose', action='store_true', help='Verbose mode')
    parser.add_argument('-v', '--version', action='version', version=f'Macal 2 interpreter v{__version__}')
    return parser

def Run():
    SetupSearchPath()
    parser = BuildArgParser()
    args = parser.parse_args()
    if args.file is None:
        parser.print_help()
        return
    if args.verbose:
        PrintBanner()
    MacalDecompiler(args.file).Decompile()


def PrintBanner() -> None:
    print(f"Macal decompiler v{__version__}")
    print(f"Author:  {__author__}")
    print(f"Email:   {__author_email__}")
    print(f"License: {__license__}")
    print()

def PrintTokens(tokens: list) -> None:
    print("Tokens:")
    for token in tokens:
        print(token)
    print()

def PrintAst(ast) -> None:
    print("AST:")
    ast.tree()
    print()

if __name__ == "__main__":
    Run()