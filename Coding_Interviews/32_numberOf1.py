# coding: utf-8

'''
从1到n整数中1出现的次数

输入一个整数n，求从1到n这n个整数的十进制表示中1出现的次数。
例如输入12，从1到12这些整数中包含1的数字有1,10,11,12。
1出现了5次
'''


def numberOf1(n):
    k = 1
    cnt, multiplier, left_part = 0, 1, n

    while left_part > 0:
        curr = left_part % 10
        right_part = n % multiplier

        cnt += (left_part / 10 + (k < curr)) * multiplier

        if k == 0 and multiplier > 1:
            cnt -= multiplier

        if curr == k:
            cnt += right_part + 1

        left_part /= 10
        multiplier *= 10

    return cnt
