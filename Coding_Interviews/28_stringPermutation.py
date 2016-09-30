# coding: utf-8

'''
输入一个字符串，打印出该字符串中字符的所有排列

例如输入字符串 abc
打印出 abc, acb, bac, bca, cab, cba
'''


def permutation(result, strs, str_list):
    if len(str_list) == 1:
        result.append(strs + str_list[0])
    else:
        for tmp_str in str_list:
            tmp_list = str_list[:]
            tmp_list.remove(tmp_str)
            permutation(result, strs + tmp_str, tmp_list)


def strPermutation(data):
    list_input = list(data)
    result = []
    permutation(result, '', list_input)
    pp = ','.join(result)
    print(pp)


if __name__ == '__main__':
    strPermutation("a")
