# -*- coding: utf-8 -*-
"""
 author: NotOne
 data:2020-08-07 10:56
"""


def BSearch(nums, target):
    """
    二分查找模版
    :param nums:
    :return:
    """
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == '__main__':
    res = BSearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
    print(res)