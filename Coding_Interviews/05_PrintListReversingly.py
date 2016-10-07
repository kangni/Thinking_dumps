# -*- coding: utf-8 -*-

# 从尾到头打印链表
# 输入一个链表的头结点，从尾到头打印出每个结点的值


class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list_reversingly(head):
    if head is not None:
        if head.next is not None:
            print_list_reversingly(head.next)
        print(head.data)


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(print_list_reversingly(head))
