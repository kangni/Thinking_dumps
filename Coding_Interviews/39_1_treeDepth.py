# coding: utf-8

'''
输入一棵二叉树的根结点，求最大树深
'''

def treeDepth(root):
    if not root:
        return 0
    return max(treeDepth(root.left), treeDepth(root.right)) + 1
