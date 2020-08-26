# -*- coding: utf-8 -*-
"""
 author: NotOne
 data:2020-08-26 14:39
"""

"""
选择排序
在遍历一次的过程中找到最小的或者最大值的索引，然后将最小值或者最大值和当前值进行交换
"""


def selectSorted(nums):
    """
    选择排序的实现
    :param nums:
    :return:
    """
    if not nums:
        return nums
    for i in range(len(nums)):
        min_idx = i
        for j in range(i, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums


if __name__ == '__main__':
    a = [12, 32, 1, 2, 1, 23, 45, 6, 7]
    res = selectSorted(a)
    print(res)