#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    i = 0
    res_list = [0] * list_length
    while i < list_length:
        try:
            div_result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            div_result = 0
            print("division by 0".format())
        except (TypeError, ValueError):
            div_result = 0
            print("wrong type".format())
        except IndexError:
            div_result = 0
            print("out of range".format())
        finally:
            res_list[i] = div_result
        i += 1
    return res_list
