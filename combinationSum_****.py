# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""


def combinationSum(nums, target):
    """
    nums中的所有数字加起来等于target，可以重复使用
    :param nums:
    :param target:
    :return:
    """
    # n = target
    nums = nums[::-1]
    res = []
    for i in range(len(nums)):
        j = i
        lis = []
        n = target
        while j < len(nums):
            if n == 0:
                res.append(lis)
                break
            if n - nums[j] < 0:
                break
                # j += 1
            else:
                n -= nums[j]
                lis.append(nums[j])
    return res
    # if n == 0:
    #     res.append(lis)
    #     pass
    # while n >= 0:
    #     if n == 0:
    #         pass
    #     for i in nums:
    #         n -= i
    #     pass


def combinationSum_answer(candidates, target):
    res = []
    candidates.sort()
    dfs(candidates, target, 0, [], res)
    return res


def dfs(nums, target, index, path, res):
    """
    深度优先遍历,
    :param nums:
    :param target:
    :param index:
    :param path:
    :param res:
    :return:
    """
    if target < 0:
        return  # backtracking
    if target == 0:
        res.append(path)
        return
    for i in range(index, len(nums)):
        if nums[i] > target:
            break
        dfs(nums, target - nums[i], i, path + [nums[i]], res)


if __name__ == '__main__':
    nums = [2, 3, 6, 7]
    target = 7
    res = combinationSum(nums, target)

    print(res)
