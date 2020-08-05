# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""

"""
爬楼梯,动态规划解题
leetcode: 70
"""


def climbStairs(n):
    """
    每次可以爬1阶或者2阶楼梯
    :param n:
    :return:
    """
    cache = [1] * n
    print(cache)
    for i in range(1, n):
        cache[i] = cache[i - 2] + cache[i - 1]
    print(cache)
    return cache[-1]


def climbStairs_xy(n):
    x, y = 1, 1
    for i in range(1, n):
        x, y = y, x + y
    return y


if __name__ == '__main__':
    res = climbStairs_xy(4)
    print(res)