# -*- coding: utf-8 -*-
"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""


class Solution:
    def climb_stairs(self, n):
        prev, cur = 0, 1
        for i in range(n):
            prev, cur = cur, prev + cur
        return cur

# another way
# climbStairs = lambda n:n if n<2 else climbStairs(n-1) + clibmStairs(n-2)
