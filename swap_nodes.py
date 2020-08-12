# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""
from common.ListNode import ListNode, printNode


def swapNode(node):
    """
    成对交换链表节点， e.g: 1->2->3->4 :::> 2->1->4->3
    :param head:
    :return:
    """
    pass

    """
    思路:
    将两个节点进行交换
    """
    new = ListNode(0)
    if not node.next:
        return node
    new.next = node.next.next
    cache = ListNode(0)
    cache.next = node.next
    cache.next.next = node
    ###忽略了节点的地址指向问题, 这样操作会在原节点上直接操作
    cache.next.next.next = None
    return cache.next,


def swapPairs(head):
    """
    :param head:
    :return:
    """
    res = ListNode()
    while head:
        swapnode = swapNode(head)
        head = head.next
        res.next = swapnode
    # res.next = swapNode(head)
    return res


def answer(head):
    dummy = pre = ListNode(0)
    pre.next = head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, a.next, b.next = b, b.next, a
        pre = a
    return dummy.next
    # prev, cur, tmp = None, head, None
    # while cur and cur.next:
    #     tmp = cur.next.next
    #     prev = cur.next.next
    #     prev.next = cur
    #     cur = tmp
    # return prev

def removeDuplicates(nums):
    """
    删除有序列表中的重复字符, 不申请其他列表空间，在原来的列表上进行操作，判断相邻两个索引位置值是否相等，不相等则将i+1的值添加到原来的列表， ##只是移动了列表中索引的位置，并没有删除列表中的值
    :param nums:
    :return:
    """
    if not nums:
        return 0
    # length = 1
    # for i in range(len(nums) - 1):
    #     if nums[i] != nums[i + 1]:
    #         nums[length] = nums[i+1]
    #         length += 1
    # return length, nums
    i, j = 0, 1
    while j < len(nums):
        if nums[i] == nums[j]:
            # j += 1
            nums.pop(j)
        else:
            i += 1
            j += 1
    return nums


def strStr(haystack, needle):
    """
    返回haystack中第一次出现needle的索引位置
    :param haystack:
    :param needle:
    :return:
    """
    if not needle:
        return 0
    # if not haystack and needle:
    #     return -1
    # if haystack and not needle:
    #     return 0
    for i in range(0, len(haystack) - len(needle) + 1):
        if haystack[i: i + len(needle)] == needle:
            return i
    return -1


def findSubstring(s, words):
    """
    查找子串的所有组合的串联词
    :param s:
    :param words:
    :return:
    """
    from collections import Counter
    if not words:
        return []
    res = []
    wordsDict = Counter(words)
    word_length = len(words[0])
    words_len = len(words)
    length = words_len * word_length
    for i in range(0, len(s) - length + 1):
        str_s = s[i: i + length]
        words_copy = wordsDict.copy()
        for j in range(0, length, word_length):
            short_str = str_s[j: j + word_length]
            if short_str not in words_copy:
                break
            else:
                words_copy[short_str] = words_copy.get(short_str, 1) - 1
                if not words_copy[short_str]:
                    words_copy.pop(short_str)

        # words_copy.sort()
        if not words_copy:
            res.append(i)
    return res


def combineWords(words):
    """
    对子串列表进行组合排列
    :param words:
    :return:
    """
    res = []
    for i in words:
        res.append(''.join(words))
    return res
    pass


if __name__ == '__main__':
    head = ListNode(0, ListNode(1, ListNode(2)))
    res = answer(head)
    printNode(res)
    # nums = [0, 1,1,1,1,1, 2,2,2,2,2,2, 3, 4, 5]
    # # nums = [1, 1, 2]
    # res = removeDuplicates(nums)
    # print(res)
    # s = "wordgoodgoodgoodbestword"
    # words = ["word","good","best","word"]
    s = "barfoothefoobarman"
    # words = ["foo", "bar"]
    # print(findSubstring(s, words))
