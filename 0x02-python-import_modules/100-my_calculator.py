#!/usr/bin/python3

if __name__ == "__main__":
    """
        use command line arguments to handle basic operations
    """
    import sys
    from sys import argv
    from calculator_1 import add, sub, mul, div

    argv = argv[1:]

    if len(argv) != 3:
        sys.stderr.write("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        exit(1)

    a = int(argv[0])
    b = int(argv[2])

    if argv[1] == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif argv[1] == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif argv[1] == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif argv[1] == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /\n")
        exit(1)
