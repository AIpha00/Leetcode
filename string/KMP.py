# -*- coding: utf-8 -*-
"""
 author: NotOne
 data:2020-08-24 14:37
"""

"""
动手实现一个KMP算法
"""


def KMP(char, partten, start=0):
    """
    利用KMP算法实现对字符串的查找
    :param char:
    :param partten:
    :return:
    """
    i, j = start, 0
    next = get_next(partten)

    while i < len(char) and j < len(partten):
        if j == -1 or char[i] == partten[j]:
            i += 1
            j += 1
        else:
            j = next[j]
    if j == len(partten):
        return i - j
    else:
        return -1


def get_next(char):
    """
    这里匹配的意义何在呢，匹配的结果是什么

    这里算出的是字符串的PMT(部分匹配表)
    已匹配的值-对应的部分匹配值 == 匹配值前缀的索引位置
    :param char:
    :return:
    """
    next = [-1] * len(char)
    i, j = 0, -1
    while i < len(char) - 1:
        if j == -1 or char[i] == char[j]:
            i += 1
            j += 1
            next[i] = j
        else:
            j = next[j]
    return next


def kmpLv(char, partten):
    """
    出自NotOne之手
    :param char:
    :param partten:
    :param start:
    :return:
    """
    i, match = 0, -1

    # 计算匹配字符的PMT值
    next = [-1] * len(partten)
    while i < len(partten) - 1:  ##这里控制前缀
        if match == -1 or partten[i] == partten[match]:
            i += 1
            match += 1
            next[i] = match
        else:
            match = next[match]  ##如果找到前缀和后缀不匹配的值时，后缀将从头开始

    i, j = 0, 0
    while i < len(char) and j < len(partten):
        if j == -1 or char[i] == partten[j]:
            i += 1
            j += 1
        else:
            j = next[j]
    if j == len(partten):
        return i - j
    return -1


if __name__ == '__main__':
    s = 'bbc abcdab abcdabcdabde'
    partten = 'abcdabd'
    res = KMP(s, partten, )
    print('标准：')
    print(res)
    res_lv = kmpLv(s, partten)
    print('我的：')
    print(res_lv)
