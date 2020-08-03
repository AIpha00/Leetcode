# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""


def search(nums, target):
    """
    在选择数组，数组以升序排列但以某个位置选择，即这个位置左边为大，右边为小，且算法运行复杂度为O(log(n))
    :param nums:
    :param target:
    :return:
    """
    # n = len(nums) // 2
    # if target > nums[0]:
    #     if target < nums[n]:
    #         search(nums[0: n], target)
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if target == nums[mid]:
            return mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        # if nums[start] > target > nums[end]:
        #     return -1
        # if nums[start] <= target <= nums[mid]:
        #     end = mid
        # elif nums[mid] <= target <= nums[end]:
        #     start = mid
        # elif nums[mid] <= target <= nums[start]:
        #     end = mid
        # elif nums[end] <= target <= nums[mid]:
        #     start = mid
        if nums[start] <= nums[mid]:
            if nums[start] < target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[mid] < target < nums[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


if __name__ == '__main__':
    res = search([1, 2, 3], 1)
    print(res)
