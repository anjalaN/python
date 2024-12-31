#!/usr/bin/env python3
import sys
if len(sys.argv[1:]) == 0:
    print("none")
    exit(0)
def shrink(arg):
        text1 = arg[0:8]
        print(text1)
def enlarge(arg):
         nbr = 8-len(arg)
         print(arg+nbr*"Z")
for arg in sys.argv[1:]:
    if len(arg) == 8:
        print(arg)
    elif len(arg) > 8:
        shrink(arg)
    else:
        enlarge(arg)