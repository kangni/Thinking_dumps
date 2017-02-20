# -*- coding: utf-8 -*-
"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""


class Solution(object):
    def lever_order(self, root):
        result = []
        if root is None:
            return result
        queue = []
        queue.append(root)
        while queue:
            n = len(queue)
            level = []
            for i in range(n):
                root = queue.pop(0)
                if root.left is not None:
                    queue.append(root.left)
                if root.right is not None:
                    queue.append(root.right)
                level.append(root.val)
            result.append(level[:])
        return result
