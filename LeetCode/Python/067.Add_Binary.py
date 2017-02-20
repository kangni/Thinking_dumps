# -*- coding: uft-8 -*-
"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""


class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def add_binary(self, a, b):
        result, carry, val = "", 0, 0
        for i in range(max(len(a), len(b))):
            val = carry
            if i < len(a):
                val += int(a[-(i + 1)])
            if i < len(b):
                val += int(b[-(i + 1)])
            carry, val = val / 2, val % 2
            result += str(val)
        if carry:
            result += str(carry)
        return result[::-1]


if __name__ == '__main__':
    result = Solution().add_binary('11', '1')
    print(result)
