#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    argv.pop(0)
    argc = len(argv)

    if (argc == 0):
        print("0 arguments.")
    elif (argc == 1):
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))

    i = 0

    for arg in argv:
        i += 1
        print("{}: {}".format(i, arg))
