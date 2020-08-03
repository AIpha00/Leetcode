# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""
"""
括号生成
leetcode： 22
"""


class Solution:
    def generateParenthesis(self, n):
        """
        生成n对合法的有效的括号组合
        Leetcode: 22
        :param n:
        :return:
        """
        """
        思路：n = 括号数 = '(' = ')' = n 左括号等于右括号等于n
        """

        """
        递归就是栈的调用
        """
        self.res = []
        self.generate(n, n, '')
        return self.res

    def generate(self, left, right, result):
        if left == 0 and right == 0:
            self.res.append(result)
            return
        if left: ##这里也是剪枝操作
            self.generate(left - 1, right, result + '(')
        if right and right > left:  ##这里进行剪枝操作
            self.generate(left, right - 1, result + ')')


if __name__ == '__main__':
    S = Solution()
    print(S.generateParenthesis(3))
