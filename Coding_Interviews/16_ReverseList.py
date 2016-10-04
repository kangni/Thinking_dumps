# -*- coding: utf-8 -*-
# 定义一个函数，输入一个链表的头结点，反转该链表并输出反转后链表的头结点


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution(object):
    def reverseList(self, head):
        res = None
        while head is not None:
            next_node = head.next
            if res is None:
                res = head
                res.next = None
            else:
                head.next = res
                res = head
            head = next_node
        return res

if __name__ == '__main__':
    head = ListNode(None)
#    head = ListNode(1)
#    head.next = ListNode(2)
#    head.next.next = ListNode(3)
#    head.next.next.next = ListNode(4)
#    head.next.next.next.next = ListNode(5)
    print(Solution().reverseList(head))
