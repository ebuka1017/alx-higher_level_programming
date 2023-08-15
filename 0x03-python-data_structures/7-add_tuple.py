#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)

    while len(a) < 2:
        a.append(0)
    while len(b) < 2:
        b.append(0)
    while len(a) > 2:
        a.pop()
    while len(b) > 2:
        b.pop()

    suml = [x + y for x, y in zip(a, b)]
    sumt = tuple(suml)
    
    return sumt
