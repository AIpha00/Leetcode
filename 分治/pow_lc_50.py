# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""
"""
分治的思想：
将一个问题分解成多个小问题，利用递归实现
leetcode: 50
"""


def pow(x, n):
    """
    利用分治实现x的n次幂
    x ** n : x * x * x * x * x * x * x * x * x ---> x ** n/2 * x ** n/2
    :param x:
    :param n:
    :return:
    """
    if n == 0:
        return 1
    if n < 0:
        return 1 / pow(x, -n)
    if n % 2:
        return x * pow(x, n - 1)
    return pow(x * x, n / 2)


def majority(nums):
    # from collections import OrderedDict
    """
    找出数组中一个数字出现的次数超过数组长度的一半，返回这个数字
    leetcode：169
    :param nums:
    :return:
    """
    """
    利用map数据结构来解
    """
    mapping = {}
    for num in nums:
        mapping[num] = mapping.get(num, 0) + 1
    return max(mapping.items(), key=lambda x: x[-1])[0]


def majority_by_divide(nums):
    """
    利用分治求解数组中的众数
    :param nums:
    :return:
    """


if __name__ == '__main__':
    # x = 2
    # n = -12
    # res = pow(x, n)
    # print(res)
    nums = [2, 3, 2, 4, 1, 3, 3, 3, 3, 3]
    majority(nums)
