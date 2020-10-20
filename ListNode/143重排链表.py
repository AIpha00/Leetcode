# -*- coding: utf-8 -*-
# @Time : 2020/10/20
# @Author : NotOne
# @Email : lvsongke@tianyancha.com


"""
将链表头尾相连重新合并

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.

leetcode:143
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head) -> None:
        """
        找到链表的中点，翻转中点链表，合并链表
        :param head:
        :return:
        """
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        pre, cur = None, slow.next

        slow.next = None

        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        res = head

        ## 合并链表：1 -> 5 -> 2
        while pre and res:
            tmp1 = res.next
            tmp2 = pre.next
            res.next = pre
            res = tmp1
            pre.next = res
            pre = tmp2
        return head