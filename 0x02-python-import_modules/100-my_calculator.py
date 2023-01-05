#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) == 4:
        val1 = int(sys.argv[1])
        val2 = int(sys.argv[3])
        if sys.argv[2] == '+':
            print("{:d} + {:d} = {:d}".format(val1, val2, add(val1, val2)))
        elif sys.argv[2] == '-':
            print("{:d} - {:d} = {:d}".format(val1, val2, sub(val1, val2)))
        elif sys.argv[2] == '*':
            print("{:d} * {:d} = {:d}".format(val1, val2, mul(val1, val2)))
        elif sys.argv[2] == '/':
            print("{:d} + {:d} = {:d}".format(val1, val2, div(val1, val2)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        exit(0)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
