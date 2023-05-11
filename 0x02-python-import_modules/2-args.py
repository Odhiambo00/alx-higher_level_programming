#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    a_list = sys.argv[1:]
    i = len(a_list)
    if i == 0:
        print("0 arguments.")
    elif i == 1:
        print("1 argument:")
        print(f"{i}: {a_list[0]}")
    else:
        print(f"{i} arguments:")
        for r in range(i):
            print(f"{r + 1}: {a_list[r]}")
