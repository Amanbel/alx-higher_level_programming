#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{:d} arguments.".format(len(sys.argv) - 1))
    else:
        for i in range(0, len(sys.argv)):
            if i == 0:
                print("{:d} arguments:".format(len(sys.argv) - 1))
                continue
            print("{:d}: {:s}".format(i, sys.argv[i]))
