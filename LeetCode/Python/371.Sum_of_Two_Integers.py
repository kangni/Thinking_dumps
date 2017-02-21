# -*- coding: utf-8 -*-
"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
"""


class Solution(object):
    def get_sum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        利用异或位操作
        ~(a & MAX_INT) ^ MAX_INT 的目的是把前面都填满1，可以只要「(~0 << 31) | a」
        """
        MOD = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFF
        while b:
            a, b = (a ^ b) & MOD, ((a & b) << 1) & MOD
        return a if a <= MAX_INT else ~(a & MAX_INT) ^ MAX_INT


if __name__ == '__main__':
    result = Solution().get_sum(-1, -2)
    print(result)
