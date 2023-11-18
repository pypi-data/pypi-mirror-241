#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#

# Interactive Line Interpreter class

from .__about__ import (
    __author__,
    __author_email__,
    __copyright__,
    __license__,
    __version__,
)
from .macal_compiler import MacalCompiler
from .macal_decompiler import MacalDecompiler
from .macal_lexer import Lexer
from .macal_parser import Parser


class MacalInteractive:
    def __init__(self) -> None:
        self.lexer: Lexer = Lexer()
        self.parser: Parser = Parser()
        self.compiler: MacalCompiler = MacalCompiler()
        self.decompiler: MacalDecompiler = MacalDecompiler(None, True)
        self.do_except: bool = True

    def ReadLine(self) -> str:
        return input(">>> ")

    def ExecuteLine(self, text: str) -> None:
        tokens = self.lexer.lex(text)
        print(tokens)
        ast = self.parser.parse_interactive(tokens)
        print(ast)
        start = self.compiler.cs.rip.value
        self.compiler.cs.flags.trap = True
        self.compiler.compile_interactive(ast)
        end = self.compiler.cs.rip.value
        print("start, end = ", start, end)
        self.decompiler.vm.memory = self.compiler.cs.memory[start:end]
        self.compiler.cs.rip.value = start
        self.decompiler.Decompile()
        while self.compiler.cs.rip.value < end:
            self.compiler.cs.Execute()
            self.compiler.cs.Halted = False
        self.compiler.cs.flags.trap = False

    def RunStep(self) -> bool:
        text = self.ReadLine()
        if text is None or text.strip() == "":
            return True
        if text == "exit":
            return False
        if text == "credits":
            print("Product:   Macal")
            print("Author:    ", __author__)
            print("Email:     ", __author_email__)
        elif text == "license":
            print("License:   ", __license__)
        elif text == "copyright":
            print("Copyright:   ", __copyright__)
        elif text == "reset":
            self.compiler.cs.Reset()
        else:
            self.ExecuteLine(text.strip())
        return True

    def Run(self) -> None:
        print("Macal Interactive Interpreter v" + __version__)
        print("Type 'exit' to exit. Type 'copyright', 'credits' or 'license' for more information.")
        self.compiler.cs.Reset()
        while True:
            if self.do_except:
                if not self.RunStep():
                    break
            else:
                try:
                    if not self.RunStep():
                        break
                except Exception as e:
                    print(e)
                    continue
