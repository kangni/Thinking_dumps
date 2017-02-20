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
        解法1在数据量大的时候效率低下
        利用位运算
        位运算的异或(^)，其中一个属性就是 n^n=0, 0^n=n。
        只要将所有的数进行异或操作就能得到只出现一次的数。
        """
        ans = 0
        for i in nums:
            ans ^= i
        return ans


if __name__ == '__main__':
    l = [2, 3, 6, 3, 2, 5, 5]
    result = Solution().single_number(l)
    print(result)
