# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""
from collections import Counter


def longest_palind(s):
    if not s:
        return s
    s_count = Counter(s)
    ##过滤掉字符串中只出现一次的值
    bnb = list(filter(lambda x: x[-1] > 1, s_count.items()))
    if not bnb:
        return s[0]
    print(bnb)
    res = s[0]
    for val, num in bnb:
        print(val, num)
        first = 0
        for _ in range(num - 1):
            first = s.find(val, first, -1)
            second = s.find(val, first + 1, -1)
            if not second < 0:
                second += 1
                if s[first: second] == s[first: second][::-1]:
                    new = s[first: second]
                    if len(new) > len(res):
                        res = new
            else:
                if s[first:] == s[first:][::-1]:
                    new = s[first:]
                    if len(new) > len(res):
                        res = new
            first = second
    return res
    pass


def answer(s):
    """

    :param s:
    :return:
    """
    if len(set(s)) <= 1:
        return s
    res = s[0]
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            if s[i: j] == s[i:j][::-1]:
                if len(s[i:j]) > len(res):
                    res = s[i:j]
    return res


def better_answer(s):
    """
    从中间向两头扩散 O(1/2 * n) 最坏: O(n * n)
    :param s:
    :return:
    """
    res = ''
    for i in range(len(s)):
        # tmp = helper(s, i, i)
        # if len(tmp) > len(res):
        #     res = tmp
        #
        # tmp = helper(s, i, i+1)
        # if len(tmp) > len(res):
        #     res = tmp
        ### helper(s, i, i), helper(s, i, i+1) 分别处理回文字符是奇偶的情况
        res = max(helper(s, i, i), helper(s, i, i + 1), res, key=len)
    return res


def helper(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l + 1: r]


def reverse_int(x):
    """
    翻转int类型的数字
    :param x:
    :return:
    """
    res = []


if __name__ == '__main__':
    s = 'bdadbafweqb'
    res = better_answer(s)
    print(res)
