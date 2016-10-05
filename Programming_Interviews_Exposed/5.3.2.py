# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def deep(root):
    if not root:
        return False
    print(root.data)
    deep(root.left)
    deep(root.right)

if __name__ == '__main__':
    tree = Node(100, Node(50, Node(25), Node(75)), Node(150, Node(125, Node(110)), Node(175)))
    deep(tree)
