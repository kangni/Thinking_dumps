# *- -coding: utf-8 -*-

# 从1到n整数中1出现的次数

# 输入一个整数n，求从1到n这n个整数的十进制表示中1出现的次数。
# 例如输入12，从1到12这些整数中包含1的数字有1,10,11,12。
# 1出现了5次


def number_of_1(n):
    k = 1
    count, multiplier, left_part = 0, 1, n

    while left_part > 0:
        curr = left_part % 10
        right_part = n % multiplier
        count += (left_part // 10 + (curr > k)) * multiplier

        if k == 0 and multiplier > 1:
            count -= multiplier
        if curr == k:
            count += right_part + 1

        left_part //= 10
        multiplier *= 10

    return count

if __name__ == '__main__':
    m = 12
    print(number_of_1(m))
