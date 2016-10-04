# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def hassubtree(p, q):
    result = False
    if p and q is None:
        return True
    elif p and q:
        if p.data == q.data:
            result = doestree1havetree2(p, q)
        if not result:
            result = hassubtree(p.left, q)
        if not result:
            result = hassubtree(p.right, q)
    return result


def doestree1havetree2(p, q):
    if q is None:
        return True
    if p is None:
        return False
    if p.data != q.data:
        return False
    return doestree1havetree2(p.left, q.left) and doestree1havetree2(p.right, q.right)

if __name__ == '__main__':
    tree1 = Node(8, Node(8, Node(9), Node(2, Node(4), Node(7))), Node(7))
    tree2 = Node(8, Node(9), Node(2))
    print(hassubtree(tree1, tree2))
