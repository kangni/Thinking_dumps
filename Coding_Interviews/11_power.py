# coding: utf-8

'''
数值的整数次方

实现函数double Power(double base, int exponent)，求base的exponent次方。
不得使用库函数，同时不需要考虑大数问题。
'''

def getPower(base, exponent):
    absExponent = exponent
    if exponent < 0:
        absExponent = -exponent

    result = powerWithUnsignedExponent(base, absExponent)
    if exponent < 0:
        result = 1.0 / result
    return result


def powerWithUnsignedExponent(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base

    result = getPower(base, exponent >> 1)
    result *= result
    if exponent & 0x1 == 1:
        result *= base


    return result
