# -*- coding: utf-8 -*-
"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
"""


class Solution(object):
    def is_power_of_four(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # find the rule
        # 二进制表示皆为1后面接n个0, n>=0
        # 二进制表示中1的位置皆在奇数位
        return (num > 0) and (num & (num - 1) == 0) and (num & 0x55555555 != 0)


if __name__ == '__main__':
    result1 = Solution().is_power_of_four(16)
    result2 = Solution().is_power_of_four(5)
    print(result1, result2)
