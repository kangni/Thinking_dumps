# -*- coding: utf-8 -*-

# 二叉树的镜像
# 完成一个函数，输入一个二叉树，该函数输出它的镜像


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def mirror_recursively(p):
    if p is None:
        return 0
    elif p.left and p.right:
        p.left, p.right = p.right, p.left
        if p.left:
            mirror_recursively(p.left)
        if p.right:
            mirror_recursively(p.right)
    return p


def lookup(root):
    stack = [root]
    while stack:
        cur = stack.pop(0)
        print('层次遍历：%s' % cur.data)
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)

if __name__ == '__main__':
    tree = Node(8, Node(6, Node(5), Node(7)), Node(10, Node(9), Node(11)))
    lookup(tree)
    print('=================')
    lookup(mirror_recursively(tree))
