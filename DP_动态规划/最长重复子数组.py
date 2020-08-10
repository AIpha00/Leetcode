# -*- coding: utf-8 -*-
"""
 author: NotOne
 data:2020-08-06 16:40
"""


def solution(A, B):
    m, n = len(A), len(B)
    dp = [[0] * (n + 1)] * (m + 1)
    res = 0
    for i in range(m):
        for j in range(n):
            if A[i] == B[j]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = 0
            res = max(res, dp[i][j])
    return res


if __name__ == '__main__':
    a = [1, 2, 3, 2, 1]
    b = [3, 2, 1, 4, 7]
    res = solution(a, b)
    print(res)
