#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arg = sys.argv
    length = len(arg) - 1

    if length > 1:
        print("{} arguments:".format(length))
        for i in range(1, length + 1):
            print("{}: {}".format(i, arg[i]))

    elif length == 0:
        print("0 argument.")

    else:
        print("1: argument:")
        print("{}: {}".format(length, arg[1]))
