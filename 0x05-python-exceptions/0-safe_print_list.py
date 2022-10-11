#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    function that prints x elements of a list 'my_list'
    """
    counter = 0
    try:
        for i in range(0, x):
            print(my_list[i], end="")
            counter += 1
    except IndexError:
        pass
    finally:
        print()
        return counter
