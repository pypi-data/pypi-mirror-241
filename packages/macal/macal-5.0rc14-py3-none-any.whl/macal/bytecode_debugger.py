#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#


# Bytecode debugging functions for Macal

from .conversion import convertToHex, convertToHexAddr
from .ast_nodetype import AstNodetype

def ShowFlags(flags) -> None:
    print('╔══════════════════════RFLAGS═══════════════════════╗')
    print(f"║     {flags}      ║")
    print('╚═══════════════════════════════════════════════════╝')
    print()

def ShowRegisters(rax, rbx, rcx, rdx, rsi, rdi, r8, r9, r10, r11, r12, r13, r14, r15, rip, rsp, rbp, flags) -> None:
    print('╔══════════════════════════RFLAGS═════════════════════════╗')
    print(f"║        {flags}         ║")
    print('╠═════╦════════════╦═════╦════════════╦═════╦═════════════╣')
    print(f"║ RIP ║ {convertToHexAddr(rip.value)} ║ RSP ║ {convertToHexAddr(rsp.value)} ║ RBP ║ {convertToHexAddr(rbp.value)}  ║")
    print('╠═════╬════════════╬═════╩════════════╩═════╩═════════════╣')
    for i in [rax, rbx, rcx, rdx, rsi, rdi, r8, r9, r10, r11, r12, r13, r14, r15]:
        type = i.type.name
        value = f'{i.value}'
        if type == 'INTEGER':
            value = f'{convertToHexAddr(i.value)}'
        if len(value) > 36:
            value = value[:23] + '...'
        print(f"║ {i.name:>3} ║ {type:<10} ║ {value:<36} ║")
    print('╚═════╩════════════╩══════════════════════════════════════╝')
    print()

def ShowStack(stack, rsp, rbp) -> None:
    n = 8
    if n > len(stack):
        n = len(stack)
    print('╔═══════╦════════════╦══════╦STACK═════╦═════╦══════════════════════════╗')
    print(f'║  RSP  ║ {convertToHexAddr(rsp.value)} ║ SIZE ║ {convertToHex(len(stack), 8)} ║ TOP ║ {convertToHex(n, 8)}                 ║')
    print(f'║  RBP  ║ {convertToHexAddr(rbp.value)} ║      ║          ║     ║                          ║')
    print('╠═══════╬════════════╬══════╩══════════╩═════╩══════════════════════════╣')
    i = rsp.value
    if len(stack) > 0:
        while True:
            if i < 0: break
            number = f'{i}'
            if i == rsp.value:
                entry = None
                type = '-'
                value = '-'
            else:
                entry = stack[i]
                type = entry[0].name
                value = f'{entry[1]}'
                if entry[0] == AstNodetype.FUNCTION:
                    value = f'{convertToHexAddr(entry[1])} (->fn)'
            if len(value) > 48:
                value = value[:45] + '...'
            rbp_ptr = '>' if i == rbp.value else ' '
            print(f"║ {rbp_ptr} {number:>3} ║  {type:<8}  ║ {value:<48} ║")
            i -= 1
    print('╚═══════╩════════════╩══════════════════════════════════════════════════╝')
    print()

def ShowMemory(memory, address: int = 0, size: int = 256) -> None:
    print("Memory:")
    for i in range(address, address + size, 16):
        print(f"    {convertToHexAddr(i)}: ", end='')
        for j in range(16):
            if i+j >= len(memory._memory):
                print("     "*(16-j), end='')
                break
            print(f"{convertToHex(memory._memory[i+j], 2, '0x')} ", end='')
        for j in range(16):
            if i+j >= len(memory._memory):
                print("     ", end='')
                break
            if memory._memory[i+j] >= 32 and memory._memory[i+j] <= 126:
                print(f"{chr(memory._memory[i+j])}", end='')
            else:
                print('.', end='')
        print()
        if i >= len(memory._memory):
            break
    print()
