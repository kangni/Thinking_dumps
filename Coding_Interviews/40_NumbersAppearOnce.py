# -*- coding: utf-8 -*-

numbers_appear_once = lambda data: list([x for x in data if data.count(x) == 1])

if __name__ == '__main__':
    l = [2, 4, 3, 6, 3, 2, 5, 5]
    print(numbers_appear_once(l))

