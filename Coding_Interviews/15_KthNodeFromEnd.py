# -*- coding: utf-8 -*-

# 输入一个链表，输出该链表中倒数第k个结点

# 本题从1开始计数，即链表尾结点是倒数第1个结点

# 例如一个链表有6个结点，从头结点开始它们的值
# 依次是1、2、3、4、5、6
# 倒数第3个结点是值为4的结点


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def kth_node_from_end(head, k):
    if not head or k == 0:
        return False
    cur = head
    for i in range(0, k-1):
        if cur.next:
            cur = cur.next
        else:
            return False
    k_behind = head
    while cur.next:
        cur = cur.next
        k_behind = k_behind.next
    return k_behind.val

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    print(kth_node_from_end(head, 1))
