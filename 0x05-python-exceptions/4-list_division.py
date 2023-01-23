#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lis = []
    for i in range(0, list_length):
        try:
            lis[i] = my_list_1[i]/my_list_2[i]
        except Exception as e:
            if (e = IndexError):
                print("out of range")
            elif (e = TypeError):
                print("wrong type")
            elif (e = ZeroDivisionError):
                print("division by 0")
            lis[i] = 0
    finally:
        return lis
