# -*- coding: utf-8 -*-
"""
 author: NotOne
 data:2020-08-26 15:13
"""

"""
快速排序：
找到一个基准点，将待排序列表以基准点分为左右两边, 然后进行递归直到所有的都排完序为止
"""


def quickSorted(nums, l, r):
    """
    快速排序
    :param nums:
    :return:
    """
    if l < r:
        q = partition(nums, l, r)
        quickSorted(nums, l, q - 1)
        quickSorted(nums, q + 1, r)


def partition(nums, l, r):
    curValue = nums[r]
    i = l - 1
    for j in range(l, r):
        if nums[j] <= curValue:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[r] = nums[r], nums[i + 1]
    return i + 1


if __name__ == '__main__':
    a = [2, 31, 1, 32, 3, 21, 4, 45, 46, 63, 421, 31]

    quickSorted(a, 0, len(a)-1)
    print(a)