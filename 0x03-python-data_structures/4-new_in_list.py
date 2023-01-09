#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        cp_my_list = my_list.copy()
        cp_my_list[idx] = element
        return cp_my_list
