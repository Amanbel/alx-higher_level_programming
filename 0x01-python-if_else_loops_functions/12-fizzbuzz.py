#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("{}".format("FizzBuzz"), end=" ")
        elif i % 3 == 0:
            print("{}".format("Fizz"), end=" ")
        elif i % 5:
            print("{}".format("Buzz"))
            if i == 100:
                print("\n")
        else:
            print(i, end=" ")
