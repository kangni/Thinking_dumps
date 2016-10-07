# -*- coding: utf-8 -*-

# 斐波那契问题

# 输入 n，求斐波那契数列的第 n 项的值


def fibonacci(n):
    a, b = 0, 1
    if n < 2:
        return n
    for i in range(0, n-1):
        a, b = b, a+b
    return b

if __name__ == '__main__':
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(2))
    print(fibonacci(3))
    print(fibonacci(4))

'''
# 台阶问题
一只青蛙一次可以跳上 1 级或 2 级台阶，求跳上 n 阶总共有多少种跳法

fib = lambda n:n if n<2 else fib(n-1)+fib(n-2)

# 变态台阶
一只青蛙一次可以跳上 1 级，也可以跳上 2 级......求跳上 n 阶总共有多少种跳法

fib = lambda n:n if n<2 else 2*fib(n-1)

# 矩形覆盖
我们可以用 2x1 的小矩形横着或者竖着去覆盖更大的矩形，请问用 2x1 的小矩形无重叠地
覆盖一个 2xN 的大矩形，总共有多少种方法

f = lambda n:n if N<3 else f(N-1)+f(N-2)
'''
