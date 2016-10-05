# -*- coding: utf-8 -*-


def tree_height(root):
    if not root:
        return False
    return 1 + max(tree_height(root.left), tree_height(root.right))

