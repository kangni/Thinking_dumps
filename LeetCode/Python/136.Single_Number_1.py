# -*- coding: utf-8 -*-
"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""


class Solution(object):
    def single_number(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return list([x for x in nums if nums.count(x) == 1])


if __name__ == '__main__':
    l = [2, 3, 6, 3, 2, 5, 5]
    result = Solution().single_number(l)
    print(result)
