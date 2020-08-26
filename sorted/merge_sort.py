# -*- coding: utf-8 -*-
"""
 author: NotOne
 data:2020-08-26 10:33
"""

"""
归并排序:
利用二分法，将待排序数组进行分割，分割到最后开始进行比较
"""


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    right, left = merge_sort(nums[mid:]), merge_sort(nums[:mid])
    res = []
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    if left:
        res += left
    elif right:
        res += right
    return res


if __name__ == '__main__':
    a = [2, 3, 1, 2, 7, 5, 0, 4, 3]
    res = merge_sort(a)

    print(res)