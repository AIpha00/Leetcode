# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""

"""
类似数字键盘的组合
"""


def answer(digits):
    if not digits:
        return []
    import functools
    ##建立映射表
    mapping = {
        '1': '',
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    ##类似向量的外积
    ## <mapping[digits[i]], mapping[digits[j]]>

    # num = len(digits)
    res = functools.reduce(lambda acc, digit: [x + y for x in acc for y in mapping[digit]], digits, [''])
    return res


if __name__ == '__main__':
    answer('257833')
