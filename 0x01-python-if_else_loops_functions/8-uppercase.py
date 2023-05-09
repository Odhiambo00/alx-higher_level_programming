#!/usr/bin/python3
def uppercase(str):
    s = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c2 = chr(ord(c) - 32)
            s = s + c2
        else:
            s = s + c
    print(f"{s}")
