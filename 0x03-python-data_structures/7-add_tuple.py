#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum = []
    for i in range(2):
        a = b = 0
        if i < len(tuple_a):
            a = tuple_a[i]
        if i < len(tuple_b):
            b = tuple_b[i]
        sum.append(a + b)
    tuple_res = sum[0], sum[1]
    return tuple_res
