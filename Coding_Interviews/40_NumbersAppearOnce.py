# -*- coding: utf-8 -*-

# 数组中只出现一次的数字

# 一个整型数组里除了两个数字之外，其他的数字都出现了两次，输出只出现一次的俩数字

numbers_appear_once = lambda data: list([x for x in data if data.count(x) == 1])

if __name__ == '__main__':
    l = [2, 4, 3, 6, 3, 2, 5, 5]
    print(numbers_appear_once(l))
