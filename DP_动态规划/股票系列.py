# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""
"""
使用动态规划，来解决买卖股票的最佳时机
leetcode: 121
"""


def maxProfit(prices):
    """
    每天只能交易一次
    :param prices:
    :return:
    """
    # 1.定义dp： dp[i]: 第i天的最大收益
    # i: 天数，j:是否持有股票
    # 2.dp方程(动态转移方程){
    # 1. buy: dp[i-1][0]-prices[i]
    # 2. sale: dp[i-1][1] + prices[i]
    # 3. wait: dp[i-1][j]
    # }
    res = 0
    if not prices:
        return 0
    mp = [[0, 0, 0]] * len(prices)
    ## 持有股票状态0：一直没有买入 1: 持有股票 2:之前持有股票现在卖了
    mp[0][0], mp[0][1], mp[0][2] = 0, -prices[0], 0
    for i in range(1, len(prices)):
        mp[i][0] = mp[i - 1][0]
        mp[i][1] = max(mp[i - 1][1], mp[i][0] - prices[1])  ##看他买入股票和卖掉股票的利益
        mp[i][2] = mp[i - 1][1] + prices[i]
        res = max(mp[i][0], mp[i][1], mp[i][2], res)
    return res


if __name__ == '__main__':
    res = [7, 1, 5, 3, 6, 4]
    print(maxProfit(res))
