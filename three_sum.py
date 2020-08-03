# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""


def threeSum(nums):
    """
    三数相加和为零、输出这三个值
    :param nums:
    :return:
    """
    num_sort = sorted(nums)
    i = len(nums) // 2
    # if


def binarySearch(array, l, r, x):
    if r < l:
        return -1
    mid = int(l + (r - l) / 2)

    if array[mid] == x:
        return mid

    elif array[mid] > x:
        return binarySearch(array, l, mid - 1, x)
    else:
        return binarySearch(array, mid + 1, r, x)


if __name__ == '__main__':
    array = [1, 23, 1, 1, 2, 4, 5]
    array.sort()
    x = 23
    result = binarySearch(array, 0, len(array) - 1, x)
    print(
        result
    )
