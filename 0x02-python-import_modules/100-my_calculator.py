#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, div, mul

    argv = sys.argv
    argv.pop(0)
    argc = len(argv)

    a, b = argv[0], argv[2]
    op = argv[1]

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)


    if (op == '+'):
        print("{} {} {} = {}".format(a, op, b, add(int(a), int(b))))
    elif (op == '-'):
        print("{} {} {} = {}".format(a, op, b, sub(int(a), int(b))))
    elif (op == '*'):
        print("{} {} {} = {}".format(a, op, b, mul(int(a), int(b))))
    elif (op == '/'):
        print("{} {} {} = {}".format(a, op, b, div(int(a), int(b))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
