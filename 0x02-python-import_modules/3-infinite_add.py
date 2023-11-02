#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arg = sys.argv
    number = len(arg) - 1

    if number == 0:
        print("{}".format(number))

    else:
        summ = 0
        for i in range(1, number + 1):
            summ += int(arg[i])

        print("{:d}".format(summ))
