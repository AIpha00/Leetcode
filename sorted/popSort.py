# -*- coding: utf-8 -*-
"""
 author: NotOne
 data:2020-08-26 14:28
"""

"""
冒泡排序
"""


def sortedPop(nums):
    """
    冒泡排序，两个依次比较
    :param nums:
    :return:
    """
    if not nums:
        return nums
    for i in range(len(nums) - 1):
        for j in range(i +1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


if __name__ == '__main__':
    a = [12, 3, 2, 4, 5, 8, 5, 3, 4]

    res = sortedPop(a)
    print(res)