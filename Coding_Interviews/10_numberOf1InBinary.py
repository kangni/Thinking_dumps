# -*- coding: utf-8 -*-

# 二进制中 1 的个数

# 输入一个整数，输出该数二进制表示中 1 的个数

# 比如把 9 表示成二进制是 1001，有 2 位是 1.
# 所以输出 2


# Way 1
def number_of_1(n):
    count = 0

    while n:
        count += 1
        # 相当于把n中的二进制表示中的最后一个1变成0
        n &= (n - 1)

    return count

if __name__ == '__main__':
    print(number_of_1(9))


# Way 2
def number_of_1(n):
    if n > 0:
        b_n = bin(n)
        count = b_n.count('1')
        print(b_n)
        return count
    elif n < 0:
        b_n = bin(~n)
        count = 8 - b_n.count('1')
        return count
    else:
        return 8
