# -*- coding: utf-8 -*-

# 输入一个英文句子，翻转句子中单词的顺序，但单词内字符顺序不变。
# 为简单起见，标点符号和普通字母一样处理。

#例如输入字符串"I am a student."，则输出"student. a am I"


def reverseSentence1(s):
    return ' '.join(reversed(s.split()))

if __name__ == '__main__':
    a_note = "I am a student."
    print(reverseSentence1(a_note))
