#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    add = 0
    for a_list in sys.argv[1:]:
        add = add + int(a_list)
    print(add)
