#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    for i in range(0, len(sys.argv)):
        if i == 0:
            print("{} arguments.".format(len(sys.argv) - 1))
            continue
        print("{}: {}".format(i, sys.argv[i]))
