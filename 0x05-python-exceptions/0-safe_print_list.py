#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for el in my_list[:x]:
            print("{}".format(el), end=""))
    except IndexError:
        pass
    finally:
        print("\n")
