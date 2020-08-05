# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""
"""
乘积最大子序列
leetcode: 152
"""


def maxProductSub(nums):
    """
    找出数组中最大的乘积子序列
    :param nums:
    :return:
    """
    """
    dp[i][2]定义：数组中子序列的最大乘积
    dp方程：dp[i][0] = dp[i-1] * nums[i]   因为存在负数所以需要对整数最大值和负数最大值进行存储，即将dp需要定义为二维数组
    dp[i][0] = max(dp[i-1][0] * nums[i], dp[i-1][1]*nums[i], nums[i]) 记录正数最大值
    dp[i][1] = min(dp[i-1][0] * nums[i], dp[i-1][1]*nums[i], nums[i]) 记录负数最大值
    """

    if not nums: return 0
    # dp = [[0, 0] for _ in range(len(nums))]  ##可以使用滚动数组，只需要申请两个数组就行
    ##只需要两个值进行记录
    dp = [[0, 0], [0, 0]]
    dp[0][1], dp[0][0], res = nums[0], nums[0], nums[0]

    for i in range(1, len(nums)):
        x, y = i % 2, (i - 1) % 2
        dp[x][0] = max(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
        dp[x][1] = min(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
        res = max(res, dp[x][0])
    return res
