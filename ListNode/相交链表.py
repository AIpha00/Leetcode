# -*- coding: utf-8 -*-
"""
 author: NotOne
 data:2020-08-26 17:07
"""

"""
返回两个链表相交的节点
leetcode: 160
"""

"""
双指针解法，很炫酷
"""

"""
这个解法有点新奇，特此记录一下
"""

from common.ListNode import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        采用双指针,太酷了，这个双指针解法太酷了，
        A length: m
        B length: n
        n < m
        当A，B走n步时,
        A 还剩下m - n步没走
        B = headA
        两个同时走m - n步，此时A指针走完
        B还剩下 m - (m - n)步
        A = headB
        此时两个指针所指剩下的链表长度相等，故一定会走到一起
        """
        A, B = headA, headB
        while A != B:
            if A:
                A = A.next
            else:
                A = headB
            if B:
                B = B.next
            else:
                B = headA
        return A
