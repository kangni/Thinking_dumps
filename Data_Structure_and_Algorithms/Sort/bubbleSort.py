# -*- coding: utf-8 -*-
def bubble_sort(l):
    for i in range(len(l)-1):
        for j in range(len(l)-1-i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

    return l

test_l = [2, 5, 1, 9, 6, 0, -4, -5, 2]
print(bubble_sort(test_l))

