# -*- coding: utf-8 -*-
"""
 author: NotOne
 data:2020-08-06 14:42
"""

"""
区域检索， 给定一个整数数组，求出数组从索引i到j范围内元素的总和
leetcode:303
"""


class NumArray:
    def __init__(self, nums):
        self.res = [0] * (len(nums) + 1)
        # self.res[0] = nums[0]
        for i in range(len(nums)):
            self.res[i+1] = nums[i] + self.res[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.res[j+1] - self.res[i]


if __name__ == '__main__':
    solution = NumArray([-2, 0, 3, -5, 2, -1])
    print(solution.sumRange(2, 5))