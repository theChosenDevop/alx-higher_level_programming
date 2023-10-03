#!/usr/bin/python3
import sys
nWrite = sys.stdout.write("and that piece of art is useful - Dora korpar, 2015-10-19\n")
if (nWrite == -1):
    sys.stderr.write("Error\n")
else:
    sys.exit(1)
