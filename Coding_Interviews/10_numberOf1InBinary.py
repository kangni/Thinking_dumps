# coding: utf-8

'''
二进制中 1 的个数

输入一个整数，输出该数二进制表示中 1 的个数
比如把 9 表示成二进制是 1001，有 2 位是 1.
所以输出 2
'''


def numberOf1(n):
    count = 0

    while n:
        count += 1
        n = (n - 1) & n

    return count


if __name__ == '__main__':
    print(numberOf1(9))
