#!/usr/bin/python3
lst = []
for i in range(1, 6):
    j = 1
    lst = []
    while (j<=i):
        lst.append(j)
        j += 1
    print(lst, end="")
    print()
