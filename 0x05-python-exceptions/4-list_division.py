#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nl = []

    for x in range(list_length):
        res = 0

        try:
            res = my_list_1[x] / my_list_2[x]
        except IndexError:
            print("{}".format("out of range"))
        except ZeroDivisionError:
            print("{}".format("division by 0"))
        except (ValueError, TypeError):
            print("{}".format("wrong type"))
        finally:
            nl.append(res or 0)
    return (nl)
