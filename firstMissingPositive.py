# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""
from functools import reduce


def firstMissingPositive(nums):
    """
    无序数组中找到缺失的最小的正整数,  自然数序列
    :param nums:
    :return:
    """
    pass
    first = 0
    # i, j = 0, 0
    # while i < j:
    #     pass
    ##先对数组排序
    for i in range(len(nums)):
        ##将每个值放到这个值应该在的索引位置
        while 0 <= nums[i] - 1 < len(nums) and nums[nums[i] - 1] != nums[i]:
            ##将这个值放到该有的位置例如，[4,5,3,2,1] nums[1]为 5， 应该在索引为值4 将两个位置的值进行交换
            tmp = nums[i] - 1
            nums[i], nums[tmp] = nums[tmp], nums[i]
    print(nums)
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1


if __name__ == '__main__':
    nums = [3, 4, -1, 1]
    res = firstMissingPositive(nums)

    print(res)
