#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    fin_list = []
    for i in range(0, list_length):
        fin_list.append(0)
    for i in range(0, list_length):
        try:
            fin_list[i] = my_list_1[i] / my_list_2[i]
        except TypeError:
            fin_list[i] = 0
            print("wrong type")
        except ZeroDivisionError:
            fin_list[i] = 0
            print("division by 0")
        except IndexError:
            fin_list[i] = 0
            print("out of range")
        finally:
            pass
    return fin_list
