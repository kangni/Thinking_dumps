# -*- coding: utf-8 -*-
"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = “hello”, return “olleh”.
"""


class Solution(object):
    def reverse_string(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


if __name__ == '__main__':
    s = "hello"
    result = Solution().reverse_string(s)
    print(result)
