#!/usr/bin/python3
num = 1
for i in range(0, 8):
    for i2 in range(num, 10):
        print("{:d}{:d}, ".format(i, i2), end="")
    num += 1
print("89")
