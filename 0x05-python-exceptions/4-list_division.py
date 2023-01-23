#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    quots = []
    for i in range(0, list_length):
        try:
            quot = my_list_1[i]/my_list_2[i]
        except IndexError:
            print("out of range")
            quot = 0
        except TypeError:
            print("wrong type")
            quot = 0
        except ZeroDivisionError:
            print("division by 0")
            quot = 0
        except Exception as e:
            pass
        finally:
            quots.append(quot)
    return quots
