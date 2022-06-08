#!/usr/bin/python3
def uniq_add(my_list=[]):
    filtered = set(my_list)
    re = 0
    for i in filtered:
        re += i
    return re
