# -*- coding: utf-8 -*-
"""
 author: NotOne
 data:2020-09-03 18:57
"""


def solution(a, b):
    if a == '' or b == '':
        return ''
    elif a[-1] == b[-1]:
        return solution(a[:-1], b[:-1]) + a[-1]
    else:
        res_a = solution(a[:-1], b)
        res_b = solution(a, b[:-1])
        if len(res_a) > len(res_b):
            return res_a
        return res_b


if __name__ == '__main__':
    res = solution('abcda', 'cda')
    print(res)
