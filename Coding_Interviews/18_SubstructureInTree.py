# -*- coding: utf-8 -*-

# 树的子结构
# 输入两棵二叉树A和B，判断B是不是A的子结构


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def has_subtree(p, q):
    result = False
    if p and q is None:
        return True
    elif p and q:
        if p.data == q.data:
            result = does_tree1_have_tree2(p, q)
        if not result:
            result = has_subtree(p.left, q)
        if not result:
            result = has_subtree(p.right, q)
    return result


def does_tree1_have_tree2(p, q):
    if q is None:
        return True
    if p is None:
        return False
    if p.data != q.data:
        return False
    return does_tree1_have_tree2(p.left, q.left) and does_tree1_have_tree2(p.right, q.right)

if __name__ == '__main__':
    a = Node(8, Node(8, Node(9), Node(2, Node(4), Node(7))), Node(7))
    b = Node(8, Node(9), Node(2))
    print(has_subtree(a, b))
