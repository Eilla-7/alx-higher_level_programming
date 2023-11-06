#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list:
        max_element = my_list[0]
        for i in my_list[1:]:
            if i > max_element:
                max_element = i
        return (max_element)

    else:
        return ("None")
