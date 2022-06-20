#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    r = []
    for i in range(0, list_length):
        value = 0
        try:
            value = my_list_1[i]/my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print('out of range')
        finally:
            r.append(value)
    return r
