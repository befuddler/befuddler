set logging enabled on
set pagination off
printf "PROGRAM_START((%#lx))\n", &program_start
b nexti_exit
commands
printf "STACK((%#lx))\n", *(long*)$rsp
python
import gdb
addr = int(gdb.parse_and_eval("(char*)&funge_space"))
mem = gdb.selected_inferior().read_memory(addr, 84*25)
print(f"FUNGE_SPACE(({mem.hex()}))")
end
end
r
