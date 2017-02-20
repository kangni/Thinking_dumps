# -*- coding: utf-8 -*-

# 二叉树的镜像

# 输入一个二叉树，输出它的镜像


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Way 1
def lookup(root):
    stack = [root]
    while stack:
        cur = stack.pop(0)
        print(cur.data)
        if cur.right:
            stack.append(cur.left)
        if cur.left:
            stack.append(cur.right)

if __name__ == '__main__':
    tree = Node(5, Node(3, Node(1), Node(4)), Node(10, Node(7), Node(12)))
    print(lookup(tree))
