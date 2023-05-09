#!/usr/bin/python3
for c in range(ord('z'), ord('a') - 1, -1):
    if c % 2 == 0:
        i = 0
    else:
        i = 32
    print("{}".format(chr(c - i)), end="")
