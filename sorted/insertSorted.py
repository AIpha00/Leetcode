# -*- coding: utf-8 -*-
"""
 author: NotOne
 data:2020-08-26 14:48
"""

"""
插入排序：
左边是排好序的，右边
"""


def insertSort(nums):
    """
    插入排序
    :return:
    """
    if not nums:
        return nums
    for i in range(1, len(nums)):
        curValue = nums[i]
        j = i

        ##让j一直往回走挨个比较，如果当前值小于比较值，就继续向前走，大于则插入
        while nums[j - 1] > curValue and j > 0:
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = curValue
        ## range(i, 0, -1) 会一直申请空间导致算法减慢
        # for j in range(i, 0, -1):
        #     if nums[j - 1] > curValue:
        #         nums[j] = nums[j - 1]
        #     else:
        #         break
        # else:
        #     nums[j - 1] = curValue
    return nums


if __name__ == '__main__':
    a = [1, 2, 3, 2, 1, 1, 2, 5, 7, 4, 5, 7, 3]

    res = insertSort(a)
    print(res)
