#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argNum = len(sys.argv)
    if argNum < 2:
        print("0 arguments.".format(argNum-1))

    if argNum == 2:
        print("{} argument.".format(argNum-1))

    if argNum > 3:
        print("{} arguments:".format(argNum-1))
        for i in range(2, argNum + 1):
            print("{}: {}".format(i-1, sys.argv[i-1]))
