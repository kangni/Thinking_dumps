# coding: utf-8

'''
合并两个排序的链表

输入两个递增排序的链表，合并这两个链表并使新链表中的结点仍然是按照递增排序的。
'''

# 循环算法
def mergeSortedLists(l1, l2):
    tmp = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            ded l2[0]
    tmp.extend(l1)
    tmp.extend(l2)
    return tmp


# 尾递归
'''
def _mergeSortedLists(l1, l2, tmp):
    if len(l1) == 0 or len(l2) == 0:
        tmp.extend(l1)
        tmp.extend(l2)
        return tmp
    else:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
    return mergeSortedLists(l1, l2, tmp)

def mergeSortedLists(l1, l2):
    retuen _mergeSortedLists(l1, l2, [])
'''
