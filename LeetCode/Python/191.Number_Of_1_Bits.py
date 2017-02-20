# -*- coding: utf-8 -*-
"""
Write a function that takes an unsigned integer and returns the number of ’1' bits \
it has (also known as the Hamming weight(https://en.wikipedia.org/wiki/Hamming_weight)).

For example, the 32-bit integer ’11' has binary representation \
00000000000000000000000000001011, so the function should return 3.
"""


class Solution:
    def number_of_1(num):
        count = 0
        while num:
            num &= num - 1
            count += 1
        return count

if __name__ == '__main__':
    print(number_of_1(11))

