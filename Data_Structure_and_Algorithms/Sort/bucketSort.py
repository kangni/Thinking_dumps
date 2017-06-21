# -*- coding: utf-8 -*-
def bucket_sort(seq):
    result = []
    bucket = [0 for x in range(max(seq)+1)]
    for i in seq:
        bucket[i] += 1
    for j in range(len(bucket)):
        while bucket[j]:
            result.append(j)
            bucket[j] -= 1
    return result