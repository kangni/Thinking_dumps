# -*- coding: utf-8 -*-

# 两个链表的公共节点
# 输入两个链表，找出它们的第一个公共节点


class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def find_first_common_node(l1, l2):
    if l1 is None or l2 is None:
        return None

    if l1.data == l2.data:
        return l1.data

    length1 = get_list_length(l1)
    length2 = get_list_length(l2)

    if length1 > length2:
        for i in range(length1 - length2):
            l1 = l1.next
    else:
        for i in range(length2 - length1):
            l2 = l2.next
    while l1 and l2:
        if l1.data == l2.data:
            return l1.data
        else:
            l1 = l1.next
            l2 = l2.next


def get_list_length(a_list):
    length = 0
    while a_list:
        length += 1
        a_list = a_list.next
    return length

if __name__ == '__main__':
    # a, b = None, None
    a = ListNode(1, ListNode(3, ListNode(5, ListNode(7, ListNode(9)))))
    b = ListNode(2, ListNode(4, ListNode(7, ListNode(9))))
    print(find_first_common_node(a, b))
