# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""

"""
不同的二叉搜索树
leetcode:96
"""


def numTree(n):
    """
    给定一个整数n， 求所有以1,2,3,4,....n为节点组成的二叉搜索树的
    :param n:
    :return:
    """
    """
    尝试用DP来解题
    """
    """
    定义dp[i]:以i为节点时，有多少种二叉搜索树
    """
    pass
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(1, n + 1):
        dp2 = []
        for j in range(1, i + 1):
            dp2.append(dp[j - 1] * dp[i - j])  ###这里可以替换成累加，减少空间复杂度
        dp[i] = sum(dp2)
        """
        dp[i]: 状态转移方程
        """
    return dp[n]


if __name__ == '__main__':
    res = numTree(4)
    print(res)
