# -*- coding: utf-8 -*-
"""
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9

to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Way 1
def lookup(root):
    stack = [root]
    while stack:
        cur = stack.pop()
        print(cur.data)
        if cur.right:
            stack.append(cur.left)
        if cur.left:
            stack.append(cur.right)

if __name__ == '__main__':
    tree = Node(4, Node(2, Node(1), Node(3)), Node(7, Node(6), Node(9)))
    print(lookup(tree))
