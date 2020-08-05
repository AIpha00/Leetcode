# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""

from common.ListNode import ListNode


def mergeTwoList(l1, l2):
    head = ListNode(0)
    if not l1 or not l2:
        return l1 or l2
    if l1.val > l2.val:
        l2.next = mergeTwoList(l1, l2.next)
        return l2
    else:
        l1.next = mergeTwoList(l1.next, l2)
        return l1


def mergeKLists(lists):
    """
    合并K个链表： 分治法，两个两个链表的合并
    :param lists:
    :return:
    """
    if not lists:
        return
    if len(lists) == 1:
        return lists.pop()
    mid = len(lists) // 2
    l = mergeKLists(lists[:mid])
    r = mergeKLists(lists[mid:])
    return mergeTwoList(l, r)
