# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""

"""
最长上升子序列
leetcode: 300
"""


def lengthOfLIS(nums):
    """
    给定一个无序的整数数组，找到其中最长上升子序列的长度, 子序列此时不需要连续
    :param nums:
    :return:
    """
    if not nums:
        return 0

    ###dp定义为1是因为本身自己要算一次
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[j] + 1, dp[i])

    return max(dp)


    pass