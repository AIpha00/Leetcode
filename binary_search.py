# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""


def binary_search(nums, target):
    """
    折半查找数字, nums is sort
    :param nums:
    :param target:
    :return:
    """
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        if nums[start] <= target <= nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def search_range(nums, target):
    """
    在排序好的数组中，找到target的第一次出现的位置和最后一次出现的位置，复杂度要求O(log(n))
    :param nums:
    :param target:
    :return:
    """
    res = []
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        # 找到小于目标值最近的值的索引位置 + 1 则是target第一次出现的位置
        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    res.append(start)
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        ## 找到大于target的最小值的索引位置 - 1 则是target最后一次出现的位置
        if nums[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
    res.append(end)
    return (res[0], res[-1]) if res[0] <= res[-1] else [-1, -1]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 5, 5, 5, 6, 8, 9]
    res = search_range(nums, 5)
    print(res)
