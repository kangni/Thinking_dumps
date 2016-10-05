# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mth_node_from_end(head, m):
    if not head:
        return False
    cur = head
    for i in range(0, m):
        if cur.next:
            cur = cur.next
        else:
            return False
    mBehind = head
    while cur.next:
        cur = cur.next
        mBehind = mBehind.next
    return mBehind.val

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(mth_node_from_end(head, 0))
