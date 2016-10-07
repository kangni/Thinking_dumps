# coding: utf-8

'''
替换空格

实现一个函数，把字符串中的每个空格替换成"%20"
例如输入"We are happy."
输出"We%20are%20happy."
'''


class Solution:
    def replace_blank(self, s):
        return s.replace(" ", "%20")
