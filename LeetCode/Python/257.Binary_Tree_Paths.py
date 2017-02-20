# -*- coding: utf-8 -*-
"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binary_tree_paths(self, root):
        result, path = [], []
        self.binary_tree_paths_recu(root, path, result)
        return result

    def binary_tree_paths_recu(self, root, path, result):
        if root is None:
            return 0
        else:
            path.append(root.val)
            if root.left is None and root.right is None:
                p = '->'.join(map(str, path))
                result.append(p)
            self.binary_tree_paths_recu(root.left, path, result)
            self.binary_tree_paths_recu(root.right, path, result)
            path.pop()
