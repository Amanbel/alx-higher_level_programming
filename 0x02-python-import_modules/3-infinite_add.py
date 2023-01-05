#!/usr/bin/python3
if __name__ == "__main__":
    import argparse
    sum = 0
    parser = argparse.ArgumentParser(description="adds every argument")
    parser.add_argument('inputs', type=int, nargs='*')
    args = parser.parse_args()

    for i in range(0, len(args.inputs)):
        sum += int(args.inputs[i])
    print(sum)
