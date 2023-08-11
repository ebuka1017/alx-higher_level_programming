#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    argv.pop(0)
    i = 0

    for arg in argv:
        i += int(arg)
    print(i)
