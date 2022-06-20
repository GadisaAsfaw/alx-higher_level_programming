#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    r = []
    for i in range(0, list_length):
        try:
            r.append(my_list_1[i]/my_list_2[i])
        except ZeroDivisionError:
            r.append(0)
            print("division by 0")
        except TypeError:
            r.append(0)
            print("wrong type")
        except IndexError:
            r.append(0)
            print('out of range')
    return r
