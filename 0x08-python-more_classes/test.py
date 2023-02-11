#!/usr/bin/python3
def display(n, m):
    for i in range(n):
        for j in range(m):
            print('#', end="")
        print()

def ret():
    return display(4, 5)

ret()
