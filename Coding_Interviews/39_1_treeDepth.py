# -*- coding: utf-8 -*-

# 输入一棵二叉树的根结点，求最大树深


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def tree_depth(root):
    if not root:
        return 0
    return max(tree_depth(root.left), tree_depth(root.right)) + 1

if __name__ == '__main__':
    tree = Node(5, Node(3, Node(2, Node(1), Node(4)), Node(10, Node(7), Node(12))))
    print(tree_depth(tree))
