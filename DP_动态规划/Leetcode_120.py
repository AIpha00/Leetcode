# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""

"""
三角形最小路径和
leetcode: 120
"""


def minimumTotal(triangle):
    """
    自顶向下找到最小的路径和，每一步只能移动到下一行中相邻的节点，i, i+1
    :param triangle:
    :return:
    """
    """
    贪心不可解，有部分选择是无法选到最小的
    """
    i = 0
    res = 0
    for num in triangle:
        if len(num) == 1:
            res += num[0]
        elif not num:
            res += 0
        else:
            if num[i] < num[i + 1]:
                res += num[i]
            else:
                res += num[i + 1]
                i += 1
    return res


def minimumTotalByDP(triangle):
    """
    用动态规划来解
    :param triangle:
    :return:
    """
    m = len(triangle)
    cache = triangle[-1]
    # while m > 1:
    #     for j in len(triangle[m - 1]):
    #         pass
    for i in range(m - 2, -1, -1):
        for j in range(len(triangle[i])):
            cache[j] = triangle[i][j] + min(cache[j], cache[j + 1])
    return cache[0]


if __name__ == '__main__':
    a = [[-1], [2, 3], [1, -1, -3]]
    print(minimumTotalByDP(a))
