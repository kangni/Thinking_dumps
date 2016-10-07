# -*- coding: utf-8 -*-

# 从尾到头打印链表
# 输入一个链表的头结点，从尾到头打印出每个结点的值


class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def rev(link):
    pre = link
    cur = link.next
    pre.next = None
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre

if __name__ == '__main__':
    l = Node(2, Node(4, Node(6, Node(8, Node(10)))))
    root = rev(l)
    while root:
        print(root.data)
        root = root.next
