# -*- coding: utf-8 -*-

# 把字符串转换成整数，即实现atoi


def str_to_int(a_str):
    INT_MAX = 2147483647
    INT_MIN = -2147483648
    result = 0

    if not str:
        return result

    i = 0
    while i < len(str) and str[i] == " ":
        i += 1

    sign = 1
    if str[i] == "+":
        i += 1
    elif str[i] == "-":
        sign = -1
        i += 1

    while i < len(str) and '0' <= str[i] <= '9':
        if result > (INT_MAX - (ord(str[i]) - ord('0'))) / 10:
            return INT_MAX if sign > 0 else INT_MIN
        result = result * 10 + ord(str[i]) - ord('0')
        i += 1

    return sign * result

if __name__ == '__main__':
    a_string = "abc"
    print(str_to_int(a_string))
