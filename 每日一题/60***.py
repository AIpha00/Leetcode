# -*- coding: utf-8 -*-
"""
 author: NotOne
 data:2020-09-05 16:18
"""

"""
排列的第k种排列，观察可知，固定i个数，剩下的排列方式还有(n-i)!种

leetcode:60
"""


def getPermutation(n: int, k: int) -> str:
    fac = [1]
    """
    固定第一个数身下的还有(n-1)!种排列
    """
    ##阶乘数
    for i in range(1, n):
        fac.append(fac[-1] * i)

    k -= 1
    valid = [1] * (n + 1)
    ans = []

    ##第几个数
    for i in range(1, n + 1):
        head = k // fac[n - i] + 1
        for j in range(1, n + 1):
            ##确认这个数是否被使用，使用则跳过！
            ###这是一种技巧

            # k属于 (1,2]-后两位(2,6]-后三位(6, 24]-后四位.....(n-1!, n!]后n位的排列方式
            head -= valid[j]
            if head == 0:
                ans.append(str(j))
                valid[j] = 0
                break
        k %= fac[n - i]
    return ''.join(ans)
