# -*- coding: utf-8 -*-

# 数值的整数次方

# 实现函数double Power(double base, int exponent)，求base的exponent次方。
# 不得使用库函数，同时不需要考虑大数问题。


def get_power(base, exponent):
    absExponent = exponent
    if exponent < 0:
        absExponent = -exponent
    result = power_with_unsigned_exponent(base, absExponent)
    if exponent < 0:
        result = 1.0 / result
    return result


def power_with_unsigned_exponent(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    result = get_power(base, exponent >> 1)
    result *= result
    if exponent & 0x1 == 1:
        result *= base
    return result

if __name__ == '__main__':
    print(get_power(2, 10))
