# -*- coding: utf-8 -*-
"""
 author: NotOne
 data:2020-08-31 14:49
"""

"""
寻找重复数: 给定一个包含n+1个整数数组，其数字都在1到n之间包括(1和n)，至少存在一个重复的整数，返回这个重复的树
leetcode: 287
"""

"""
空间复杂度在o(n)
时间复杂度小于O(n2)
"""

"""
这道题有特定条件，其中数字在1到n之间，可以将数组中的数字作为索引使用
"""


def findDuplicate(nums):
    """
    快慢指针
    :param nums:
    :return:
    """
    """
    因为nums中的值属于[1, n]类似与链表的next指向，所以可以用链表的快慢指针进行求解
    """
    slow, fast = nums[0], nums[nums[0]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


def findDuplicateByBS(nums):
    """
    二分法求解，太过晦涩，不好理解
    :param nums:
    :return:
    """
