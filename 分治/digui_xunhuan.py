# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""

"""
递归和循环的相互转换
"""


def fact(n):
    """
    循环版
    :param n:
    :return:
    """
    res = 1
    for i in range(1, n + 1):
        res = res * i

    return res


def fact_digui(n):
    """
    递归版
    :param n:
    :return:
    """

    """
    1.递归函数的功能—>需要做什么事
    2.找出递归结束的条件—>递归退出的终止条件
    3.找出函数的等价关系式——>每个操作都能用这个函数进行表达
    """
    if n == 1:  ##递归退出的终止条件
        return 1
    return n * fact_digui(n - 1)  ##函数等价关系式


def divingBoard(shorter, longer, k):
    """
    跳水板
    leetcode: 面试题16.11
    :param shorter:
    :param longer:
    :param k:
    :return:
    """
    if (k <= longer):
        return k
    return divingBoard(shorter, longer, k - shorter) + divingBoard(shorter, longer, k - longer)


if __name__ == '__main__':
    # res = fact(5)
    #
    # print(res)

    res_div = divingBoard(1, 2, 3)
    print(res_div)
