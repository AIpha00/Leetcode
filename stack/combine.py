# -*- coding: utf-8 -*-
"""
 author: NotOne
 data:2020-09-08 11:40
"""
"""
组合，返回1.....n中所有可能的k个数的组合
leetcode:77
"""


def combine(n: int, k: int):
    if not k or not n:
        return []
    ###回溯算法
    res = []

    def backtrance(i, k, tmp):
        if k == len(tmp):
            res.append(tmp[:])
            return
        for j in range(i, n + 1):

            ##做选择
            tmp.append(j)
            ##这里会重新返回一个新的数组，且不会修改原来的数组
            tmp + [j]
            backtrance(j + 1, k, tmp)
            tmp.pop()

    backtrance(1, k, [])
    return res


if __name__ == '__main__':
    n, k = 4, 2
    res = combine(n, k)

    print(res)