# -*- coding: utf-8 -*-
"""
 author: NotOne
 data:2020-08-19 10:56
"""
"""
计算一个字符串有多少个回文字串
leetcode: 647
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        动态规划
        :param s:
        :return:
        """
        if not s:
            return 0

    def countSubstringsByBL(self, s: str) -> int:
        """
        暴力解法，试着用动态规划来解
        :param s:
        :return:
        """
        if not s:
            return 0
        length = len(s)
        res = 0
        window = 1
        while window < length + 1:
            left = 0
            while (left + window) < length + 1:
                if s[left: left + window] == s[left: left + window][::-1]:
                    res += 1
                left += 1
            window += 1
        return res
        pass


if __name__ == '__main__':
    S = Solution()
    res = S.countSubstrings('aaa')
    print(res)
    pass
