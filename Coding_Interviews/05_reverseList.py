# coding: utf-8

'''
从尾到头打印链表

输入一个链表的头结点，从尾到头打印出每个结点的值
'''

class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def rev(link):
    pre = link
    cur = link.next
    pre.next = None
    while cur:
        tmp = current
        current = pre
        pre = cur
        cur = tmp
    return pre

root = rev(link)
while root:
    print(root.data)
    root = root.next
