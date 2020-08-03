# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""
"""
找到最长的共同前缀
"""


def longestCommonPrefix(strs):
    """
    愚蠢！不用找到所有的值，只需要找到最长的索引
    :param strs:
    :return:
    """
    if not strs:
        return ''
    min_str = min(strs, key=len)
    res = []
    for i, val in enumerate(min_str):
        if len(list(filter(lambda x: x[i] == val, strs))) != len(strs):
            break
        else:
            res.append(val)
    return ''.join(res)
