# coding: utf-8

'''
重建二叉树

输入某二叉树的前序和中序遍历的结果，请重建出该二叉树

假设输入的前序和中序遍历的结果都不含重复的数字

例如：
前序遍历序列{1, 2, 4, 7, 3, 5, 6, 8}
中序遍历序列{4, 7, 2, 1, 5, 3, 8, 6}
'''


def rebuild(pre, center):
    if not pre:
        return 0
    cur = Node(pre[0])
    index = center.index(pre[0])
    cur.left = rebuild(pre[1:index + 1], center[:index])
    cur.right = rebuild(pre[index + 1:], center[index + 1:])
    return cur


def deep(root):
    if not root:
        return 0
    deep(root.left)
    deep(root.right)
    print(root.data)
