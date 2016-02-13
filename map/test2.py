#!/usr/bin/env python3

var1 = [20,21,22,23,24,25,26,27,28,29,30]
def reverse(list1):
    ## this function:
    ##    takes a list
    ##    and returns another list reversed
    list_length = len(list1)
    results = []
    for x in range(list_length-1, -1, -1):
        results.append(list1[x])
    return results

print(reverse(var1))