# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def mirrorrecursively(p):
    if p is None:
        return 0
    elif p.left and p.right:
        p.left, p.right = p.right, p.left
        if p.left:
            mirrorrecursively(p.left)
        if p.right:
            mirrorrecursively(p.right)
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
    lookup(mirrorrecursively(tree))
