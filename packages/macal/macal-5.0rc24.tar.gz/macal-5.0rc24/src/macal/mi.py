#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#

# This is the new Macal Interpreter, it will lex, parse, compile and interpret (execute).

import argparse
import os

from macal.__about__ import __author__, __author_email__, __license__, __version__
from macal.config import SearchPath
from macal.macal_compiler import MacalCompiler
from macal.macal_decompiler import MacalDecompiler
from macal.macal_lexer import Lexer
from macal.macal_parser import Parser

import pyximport; pyximport.install()
from .cmacal_vm import MacalVm

bytecode_extension = ".mbc"
source_extension = ".mcl"


def SetupSearchPath():
    search_path = [
        os.path.dirname(__file__),
        os.path.join(os.path.dirname(__file__), "lib"),
        os.path.join(os.path.dirname(__file__), "lib", "ext"),
        os.getcwd(),
        os.path.join(os.getcwd(), "lib"),
        os.path.join(os.getcwd(), "lib", "ext"),
    ]
    for path in search_path:
        if path not in SearchPath:
            SearchPath.append(path)


def check_file(file) -> str:
    if file is None:
        return
    if not file.endswith(bytecode_extension) and not file.endswith(source_extension):
        if os.path.exists(f"{file}{source_extension}"):
            file = f"{file}{source_extension}"
        else:
            raise Exception("Invalid Macal source file.")
    return file


def BuildArgParser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Macal interpreter")
    parser.add_argument("file", nargs="?", type=check_file, help="Macal file")
    parser.add_argument("-d", "--decompile", action="store_true", help="Execute decompiler")
    parser.add_argument("-i", "--interactive", action="store_true", help="Interactive mode")
    parser.add_argument("-n", "--noexec", action="store_true", help="Do not execute")
    parser.add_argument("-o", "--output", help="Output file")
    parser.add_argument("-p", "--profile", action="store_true", help="Profile mode")
    parser.add_argument("-r", "--reserved", help="a csv list of reserved variables", default="", required=False, type=str)
    parser.add_argument("-s", "--verbose", action="store_true", help="Verbose mode")
    parser.add_argument("-v", "--version", action="version", version=f"Macal 2 interpreter v{__version__}")
    return parser


def LoadSource(fileName) -> str:
    with open(fileName, "r") as f:
        text = f.read()
    return str(text)


def Execute(filename: str, profile: bool = False) -> int:
    vm = MacalVm(filename)
    if profile:
        import cProfile
        import pstats

        with cProfile.Profile() as pr:
            vm.Execute()
        result = pstats.Stats(pr)
        result.sort_stats("cumulative")
        result.print_stats()
    else:
        vm.Execute()
    return vm.stack[0][1]


def FromExecutable(args, file: str) -> None:
    if args.decompile:
        MacalDecompiler(file).Decompile()
    if not args.noexec:
        ShowResult(Execute(file, args.profile))


def FromSource(args, file: str, output_filename: str) -> None:
    source = LoadSource(file)
    tokens = Lexer(source).tokenize()
    if args.verbose:
        PrintTokens(tokens)
    ast = Parser(tokens, args.file).parse()
    if args.verbose:
        PrintAst(ast)
    reserved = None
    if args.reserved != "":
        reserved = args.reserved.split(",")
    MacalCompiler(program=ast, output_path=output_filename, verbose=args.verbose, reserved_vars=reserved).compile()
    if args.decompile:
        MacalDecompiler(output_filename).Decompile()
    if not args.noexec:
        ShowResult(Execute(output_filename, args.profile))


def ShowResult(exitCode: int) -> None:
    if exitCode == 0:
        print("Process exits OK")
    else:
        print(f"Process exits with error: {exitCode}")
    exit(exitCode)


def Run():
    SetupSearchPath()
    parser = BuildArgParser()
    args = parser.parse_args()
    if args.interactive:
        print("Interactive mode is not available yet.")
        return
        from macal.macal_interactive import MacalInteractive

        MacalInteractive().Run()
        return
    if args.file is None:
        parser.print_help()
        return
    output_filename = str(args.output or args.file.replace(source_extension, bytecode_extension))
    if args.file.endswith(bytecode_extension):
        FromExecutable(args, args.file)
        return
    FromSource(args, args.file, output_filename)


def PrintBanner() -> None:
    print(f"Macal interpreter v{__version__}")
    print(f"Author:  {__author__}")
    print(f"Email:   {__author_email__}")
    print(f"License: {__license__}")


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
