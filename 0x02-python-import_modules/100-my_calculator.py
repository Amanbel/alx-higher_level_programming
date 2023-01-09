#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    argv = sys.argv[1:]
    argc = len(argv)
    ops = ["+", "*", "/", "-"]
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if str(sys.argv[2]) not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        val1 = int(sys.argv[1])
        val2 = int(sys.argv[3])
        if str(sys.argv[2]) == "+":
            print("{:d} + {:d} = {:d}".format(val1, val2, add(val1, val2)))
        elif str(sys.argv[2]) == "-":
            print("{:d} - {:d} = {:d}".format(val1, val2, sub(val1, val2)))
        elif str(sys.argv[2]) == "*":
            print("{:d} * {:d} = {:d}".format(val1, val2, mul(val1, val2)))
        elif str(sys.argv[2]) == "/":
            print("{:d} / {:d} = {:f}".format(val1, val2, div(val1, val2)))
