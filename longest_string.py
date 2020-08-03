# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""

from collections import Counter


def longest_string(s):
    '''
    把所有子字符都找出来了，但不用，只需要找出最长字符串的索引位置
    :param s:
    :return:
    '''
    if len(s) <= 1:
        return len(s)
    res = []
    dd = {}
    lis = list(s)
    while len(lis) > 1:
        res = []
        for s_i in lis:
            if s_i in res:
                dd[''.join(res)] = len(res)
                res = []
                res.append(s_i)
            else:
                res.append(s_i)
        dd[''.join(res)] = len(res)
        lis.pop(0)
    return max(dd.values())
    pass


def anwer(s):
    """
    找到最长子字符
    :param s:
    :return:
    """
    """
    记录出每个字符出现的索引位置
    """
    """
    滑动窗口！！！
    """
    dd = {}
    max_length = start = 0
    for i, s_i in enumerate(s):
        if s_i in dd:
            su = dd[s_i] + 1  ## 将起始位置向后移一位
            if su > start:
                start = su
        num = i - start + 1
        max_length = max(num, max_length)
        dd[s_i] = i

    return max_length


if __name__ == '__main__':
    s = "zavafc"
    res = anwer(s)
    print(res)
