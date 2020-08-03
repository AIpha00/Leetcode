# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""
"""
给定一个整数数组nums，找到一个具有最大和的连续子树组(子数组最少包含一个元素)， 返回其最大和

leetcode: 53
"""


def maxSubArray(nums):
    """
    使用O(n)复杂度来求解
    :param nums:
    :return:
    """
    # jj = 0
    # ii = 0
    # maxNum = 0
    # while ii <= jj:
    #     cur = maxNum + nums[jj]
    #     if cur < 0:
    #         maxNum = 0
    #         ii += 1
    #     if jj >= len(nums):
    #         jj = ii
    #     jj += 1
    #     maxNum = max(cur, maxNum)
    # return maxNum
    maxSum = tempSum = nums[0]
    for num in nums[1:]:
        ##相加起来小于当前的值，则tempSum = current_num
        ##贪心算法，当前的指针所指的元素之前的和小于当前指针所指的数，则丢弃当前元素之前的数列
        tempSum = max(num, num + tempSum)
        maxSum = max(maxSum, tempSum)
    return maxSum
    pass


def maxSubArrayByDivice(nums):
    """
    采用分治的思想来解题
    :param nums:
    :return:
    """
    n = len(nums)
    if n == 1:
        return nums[0]
    else:
        ##递归计算左半边最大子序和
        max_left = maxSubArrayByDivice(nums[0: len(nums) // 2])
        ##递归计算右半边最大子序和
        max_right = maxSubArrayByDivice(nums[len(nums) // 2: len(nums)])

    ##计算中间的最大子序和，从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
    max_l = nums[len(nums) // 2 - 1]
    tmp = 0
    for i in range(len(nums) // 2 - 1, -1, -1):
        tmp += nums[i]
        max_l = max(tmp, max_l)

    max_r = nums[len(nums) // 2]
    tmp = 0
    for i in range(len(nums) // 2, len(nums)):
        tmp += nums[i]
        max_r = max(tmp, max_r)

    return max(max_right, max_left, max_r + max_l)


def maxSubArrayByDP(nums):
    """
    动态规划求解
    :param nums:
    :return:
    """
    n = len(nums)

    for i in range(1, n):
        if nums[i - 1] > 0:  ##若前一个元素大于0， 则将其加到当前元素上
            nums[i] += nums[i - 1]
    return max(nums)


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = maxSubArray(nums)
    print(res)
