# -*- coding: utf-8 -*-

# 圆圈中最后剩下的数字(约瑟夫环问题)

# 0,1,...,n-1这n个数字排成一个圆圈，从数字0开始每次从这个圆圈里删除第m个数字
# 求这个圆圈里剩下的最后一个数字

# 例如，0,1,2,3,4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字
# 则删除的前四个数字依次是2,0,4,1
# 最后剩下的数字是3


class Queue:
    def __init__(self):
        self.val = []

    def is_empty(self):
        return self.val == []

    def enqueue(self, val):
        self.val.insert(0, val)

    def dequeue(self):
        return self.val.pop()

    def size(self):
        return len(self.val)


def last_remaining(numbers, m):
    num_queue = Queue()
    for number in numbers:
        num_queue.enqueue(number)
    while num_queue.size() > 1:
        for i in range(m-1):
            num_queue.enqueue(num_queue.dequeue())
        num_queue.dequeue()
    return num_queue.dequeue()

if __name__ == '__main__':
    n = [0, 1, 2, 3, 4]
    print(last_remaining(n, 3))
