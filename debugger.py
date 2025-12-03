#!/usr/bin/env python3
from pathlib import Path
import time
import re

WIDTH = 80
HEIGHT = 25


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
    for i in range(HEIGHT):
        start = (WIDTH + 4) * i
        end = start + WIDTH
        script.append(
            "".join(
                " " if not 32 <= c <= 127 else chr(c) for c in funge_space[start:end]
            )
        )

    offset = addr - program_start
    offset_instrs = offset // 10
    yy, xx = divmod(offset_instrs, WIDTH + 4)

    RED = "\033[41m"
    RESET = "\033[0m"
    CLEAR = "\033[2J\033[H"

    screen = ""
    for y, line in enumerate(script):
        for x, c in enumerate(line):
            if (y, x) == (yy, xx):
                screen += f"{RED}{c}{RESET}"

            else:
                screen += f"{c}"
        screen += "\n"
    print(f"{CLEAR}{screen}", end="")


while True:
    render()
    time.sleep(0.01)
