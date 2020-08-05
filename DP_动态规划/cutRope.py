# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""
"""
剪绳子
leetcodeL 剑指offer 14-||
"""


def cuttingRope(n):
    """
    剪
    :param n:
    :return:
    """
    if n <= 1:
        return n

    dp = list(range(n + 1))   ###dp里存的是最坏的情况，也就是将n分为(1, n-1)
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i - j] * dp[j], dp[i])
    if n <= 3:
        return dp[n] - 1
    return dp[n] % 1000000007


if __name__ == '__main__':
    res = cuttingRope(15)
    print(res)
