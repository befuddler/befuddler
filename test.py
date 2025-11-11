#!/usr/bin/env python3
import subprocess

subprocess.run(["./compiler.py", "befucked.bf"], check=True, capture_output=True)
print("Compiled")

result = subprocess.run(
    ["./befucked"], input=b"bctf{wrong_flag}\n", check=True, capture_output=True
)
print("With wrong input: ", result.stdout)
assert b"NOPE" in result.stdout

result = subprocess.run(
    ["./befucked"], input=b"bctf{thx_Mewski}\n", check=True, capture_output=True
)
print("With correct input: ", result.stdout)
assert b"Correct" in result.stdout
