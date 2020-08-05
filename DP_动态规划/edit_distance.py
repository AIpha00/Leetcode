# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""

"""
编辑距离
leetcode: 72
"""
import numpy as np


def sulotion(word1, word2):
    """
    将word1转换成word2需要最少的操作数
    :param word1:
    :param word2:
    :return:
    """
    m, n = len(word1), len(word2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    ##初始化dp table中的值，存的是最坏的情况
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    print(np.asarray(dp))
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # if word1[i - 1] == word2[j - 1]:
            #     dp[i][j] = min(dp[i - 1][j - 1] + 0, dp[i - 1][j] + 1, dp[i][j - 1] + 1)
            # else:
            insert = dp[i - 1][j] + 1
            delete = dp[i][j - 1] + 1
            replace = dp[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1)
            dp[i][j] = min(insert, delete, replace)

            # dp[i][j] = min(dp[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1),
            #                dp[i - 1][j] + 1,
            #                dp[i][j - 1] + 1)
            # print(dp[i][j])
            # dp[i][j] =
            pass

    return dp[m][n]


if __name__ == '__main__':
    res = sulotion('intention', "execution")

    print(res)
