# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""

"""
使用动态规划，求解斐波拉契数列
"""


def fib(n):
    cache = list(range(n + 1))

    for i in range(n + 1):
        if i < 2:
            cache[i] = i
        else:
            cache[i] = cache[i - 1] + cache[i - 2]
    return cache[n]


if __name__ == '__main__':
    res = fib(10000)

    print(res)
