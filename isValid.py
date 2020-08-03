# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""

"""
判断()[]是否正确
"""


def is_valid(s):
    from functools import reduce
    mapping = {
        '(': 1,
        '[': 2,
        '{': 3,
        ')': -1,
        ']': -2,
        '}': -3,
    }
    if not s:
        return False
    int_s = list(map(lambda x: mapping[x], s))
    if sum(int_s):
        return False

    n = len(int_s)
    if max(int_s[:n // 2]) < 0 or max(int_s[n // 2:]) > 0:
        return False

    i = 0
    while i < n:
        if int_s[i] + int_s[i + 1] == 0:
            if i + i + 1 + 1 == n:
                break
            else:
                i += 2
        elif int_s[i] + int_s[n - 1 - i] == 0:
            i += 1
        else:
            return False

    return True


def answer(s):
    """
    )}]只会出现在({[的后面
    :param s:
    :return:
    """
    stack, match = [], {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in match:
            if not (stack and stack.pop() == match[ch]):
                return False
        else:
            stack.append(ch)
    return not stack


if __name__ == '__main__':
    res = is_valid('()[]{}')
    print(res)
