# -*- coding: utf-8 -*-

# 从上往下打印二叉树

# 从上往下打印二叉树的每个结点，同一层的结点按照从左到右的顺序打印


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
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)

if __name__ == '__main__':
    tree = Node(5, Node(3, Node(1), Node(4)), Node(10, Node(7), Node(12)))
    print(lookup(tree))

# Way 2
'''
def from_top_to_bottom(root):
    result = []
    if not root:
        return 0
    queue = [root]
    while queue:
        n = len(queue)
        level = []
        for i in range(n):
            root = queue.pop(0)
            if root.left is not None:
                queue.append(root.left)
            if root.right is not None:
                queue.append(root.right)
            level.append(root.data)
        result.append(level)
    return result


if __name__ == '__main__':
    print(from_top_to_bottom(tree))
'''
