# -*- coding: utf-8 -*-
"""
 author: NotOne
 data:2020-08-26 17:55
"""

"""
返回数组中第K个最大的元素
"""


###用堆
def findK(nums, k):
    import collections
    dq = collections.deque(k)
    dq.append(nums[0])
    for num in nums:
        if num >= dq[-1] and len(dq) == k:
            dq.popleft()
            dq.append(num)
        elif len(dq) == k:
            i = len(dq) - 1
            while i > 0:
                if num > dq[i]:
                    dq[i], dq[i - 1] = num, dq[i]
                    i -= 1
                    j = i
                    while j > 0:
                        dq[j - 1] = dq[j]
                        j -= 1
        else:
            if num >= dq[-1]:
                dq.append(num)
            else:
                i = len(dq)
                while i > 0:
                    if num < dq[i]:
                        i -= 1


def findTopK(nums, k):
    """
    返回最大的第K的元素
    :param n:
    :return:
    """
    ###用堆作为数据结构
    import heapq
    newNums = heapq.nlargest(k, nums)
    return newNums[-1]


if __name__ == '__main__':
    nums = [1, 2, 3, 2, 1, 8, 6, 5, 9, 3, 3, 5, 6]
    k = 4
    res = findTopK(nums, k)
    print(res)
