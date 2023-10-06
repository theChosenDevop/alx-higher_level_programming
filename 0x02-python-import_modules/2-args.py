#!/usr/bin/python3

if __name__ == "__main__":
    """
    print command line argument with argument count
    """
    from sys import argv

    count = len(argv) - 1

    if count == 0:
        print("{} arguments.".format(count))
    elif count == 1:
        print("{} argument:".format(count))
    else:
        print("{} arguments:".format(count))

    for i in range(count):
        print("{}: {}".format(i + 1, argv[i + 1]))
