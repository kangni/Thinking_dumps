# -*- coding: utf-8 -*-
"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = “hello”, return “holle”.

Example 2:
Given s = “leetcode”, return “leotcede”.
"""


class Solution(object):
    def reverse_vowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        string = list(s)
        l, r = 0, len(s)-1
        while l < r:
            if string[l].lower() not in vowels:
                l += 1
            elif string[r].lower() not in vowels:
                r -= 1
            else:
                string[l], string[r] = string[r], string[l]
                l += 1
                r -= 1
        return ''.join(string)


if __name__ == '__main__':
    s = "LeetCode"
    result = Solution().reverse_vowels(s)
    print(result)
