# -*- coding: utf-8 -*-


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
