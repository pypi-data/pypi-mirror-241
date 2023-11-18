#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      09-11-2023
#
# Copyright 2023 Westcon-Comstor
#

# This is the new Macal Runtime, it interpret/execute a compiled Macal (.mbc) file.

import argparse
import os

from .__about__ import __author__, __author_email__, __license__, __version__
from .config import SearchPath

import pyximport; pyximport.install()
from .cmacal_vm import MacalVm

bytecode_extension = ".mbc"


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
    if not file.endswith(bytecode_extension):
        if os.path.exists(f"{file}{bytecode_extension}"):
            file = f"{file}{bytecode_extension}"
        else:
            raise Exception("Invalid Macal bytecode file.")
    return file


def BuildArgParser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Macal runtime")
    parser.add_argument("file", nargs="?", type=check_file, help="Macal bytecode file (.mbc)")
    parser.add_argument("-v", "--version", action="version", version=f"Macal 2 runtime v{__version__}")
    return parser


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
    if args.file is None:
        parser.print_help()
        return
    vm = MacalVm(args.file)
    vm.Execute()
    ShowResult(vm.stack[0][1])


if __name__ == "__main__":
    Run()
