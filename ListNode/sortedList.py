# -*- coding: utf-8 -*-
"""
 author: NotOne
 data:2020-08-26 14:18
"""

"""
链表归并排序算法
"""
from common.ListNode import ListNode


def sortedList(head):
    """
    归并链表排序
    :param head:
    :return:
    """
    if not head:
        return head

    def merge_sorted(head):
        if not head.next:
            return head
        mid = findMid(head)
        left, right = merge_sorted(head), merge_sorted(mid)
        cur_node = new_head = ListNode(0)
        while left and right:
            if left.val < right.val:
                cur_node.next = left
                left = left.next
            else:
                cur_node.next = right
                right = right.next
            cur_node = cur_node.next
        if left:
            cur_node.next = left
        if right:
            cur_node.next = right
        return new_head.next

    return merge_sorted(head)


def findMid(head):
    """
    找到链表中间值
    :param head:
    :return:
    """
    fast, slow = head, head
    while fast and fast.next:
        cur = slow
        fast = fast.next.next
        slow = slow.next
    if cur:
        cur.next = None
    return slow
