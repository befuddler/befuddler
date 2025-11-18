#!/usr/bin/env python3
from pathlib import Path
import time
import re


def render():
    log = Path("./gdb.txt").read_text()

    addr = 0
    for match in re.finditer(r"STACK\(\(0x([0-9a-f]+)\)\)", log):
        addr = int(match[1], 16)

    program_start = 0
    for match in re.finditer(r"PROGRAM_START\(\(0x([0-9a-f]+)\)\)", log):
        program_start = int(match[1], 16)

    funge_space = b""
    for match in re.finditer(r"FUNGE_SPACE\(\(([0-9a-f]+)\)\)", log):
        funge_space = bytes.fromhex(match[1])

    script = []
    for i in range(25):
        script.append(
            "".join(
                " " if c == 0xFF else chr(c) for c in funge_space[82 * i : 82 * i + 80]
            )
        )

    offset = addr - program_start
    offset_instrs = offset // 10
    yy, xx = divmod(offset_instrs, 82)
    print(yy, xx)

    RED = "\033[41m"
    RESET = "\033[0m"
    CLEAR = "\033[2J\033[H"

    print(CLEAR)
    for y, line in enumerate(script):
        for x, c in enumerate(line):
            if (y, x) == (yy, xx):
                print(f"{RED}{c}{RESET}", end="")
            else:
                print(f"{c}", end="")
        print()


while True:
    render()
    time.sleep(0.01)
