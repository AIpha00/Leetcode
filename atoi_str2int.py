# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""


def myatoi(x):
    x = list(x.lstrip())

    if not x:
        return 0

    if not x[0].isdigit() and x[0] not in ['+', '-']:
        return 0
    sign = 1
    if x[0] == '-':
        sign = -1
    if not x[0].isdigit():
        del x[0]
    res = 0
    idx = 0
    while idx < len(x) and x[idx].isdigit():
        res = res * 10 + ord(x[idx]) - ord('0')
        idx += 1
    return max(-2 ** 31, min(sign * res, 2 ** 31 - 1))
    pass


if __name__ == '__main__':
    res = myatoi('    -42')
    print(res)
