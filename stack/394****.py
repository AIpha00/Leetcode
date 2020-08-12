# -*- coding: utf-8 -*-
"""
 author: NotOne
 data:2020-08-12 12:05
"""

"""
字符串解码，给定字符串为"3[abc2[ac]]"
leetcode: 394
"""


def decodeString(s):
    """
    给一个经过编码的字符串，返回它解码后的字符串

    ！！错误思路，在栈里只存了一个状态，这样导致[]内嵌的[]无法计算，无法满足所有测试样例
    :param s:
    :return:
    """
    stack = []
    res = ''
    multi = 0
    for c in s:
        if c == '[':
            ##因为编码格式是3[a2[c]]这样的格式所以，栈里存的是当前的num和上一个子字符
            stack.append([multi, res])
            res, multi = '', 0
        elif c == ']':
            cur_multi, last_res = stack.pop()
            res = last_res + cur_multi * res
        elif '0' <= c <= '9':
            multi = multi * 10 + int(c)
        else:
            res += c
    return res


if __name__ == '__main__':
    s = '3[a]2[bc]'
    res = decodeString(s)
    print(res)
