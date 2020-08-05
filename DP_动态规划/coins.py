# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""
"""
给定数量不限的硬币，币值25，10， 5， 1求出n有几种表示法
leetcode: 面试题08.11
"""


def waysToChange(n):
    if n <= 1:
        return 1

    coins = [1, 5, 10, 25]
    dp = [1] + [0] * n  ##dp[i]定义： i时有多少种表示法
    for coin in coins:
        for i in range(coin, n+1):
            dp[i] += dp[i - coin]  ##dp[i] = dp[i-coin] + dp[i]
    return dp[n] % 1000000007


if __name__ == '__main__':
    print(waysToChange(10))
