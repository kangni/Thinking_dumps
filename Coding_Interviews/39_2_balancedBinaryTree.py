# -*- coding: utf-8 -*-

# 输入一棵二叉树的根结点，判断该树是不是平衡二叉树。

# 平衡二叉树：任意结点的左右子树的深度相差不超过1


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def is_balanced(root):
    if not root:
        return True
    else:
        if is_balanced(root.left) and is_balanced(root.right):
            return abs(depth(root.left) - depth(root.right)) <= 1
        else:
            return False


def depth(root):
    if not root:
        return False
    return max(depth(root.left), depth(root.right)) + 1


if __name__ == '__main__':
    tree = Node(1, Node(2, Node(4), Node(5, Node(7))), Node(3, Node(6)))
    print(is_balanced(tree))
