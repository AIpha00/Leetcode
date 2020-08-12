# -*- coding: utf-8 -*-
"""
 author: NotOne
 data:2020-08-11 17:40
"""

"""
删除链表中连续子序列等于0的子链表
leetcode: 1171
"""
from common.ListNode import ListNode


def removeZeroSumSubList(head):
    if not head or not head.next:
        return head
    stack1 = []
    stack2 = []
    tmp = 0
    while head:
        stack1.append(head)
        head = head.next
    while stack1:
        node = stack1.pop()
        tmp += node.val
        if tmp > 0:
            tmp = 0
            stack2.append(node)
        elif tmp + node.val == 0:
            ##删除节点操作
            if not stack2:
                stack1.pop().next = None
            else:
                stack1.pop().next = stack2.pop()
    return head


def removeZeroSumSublists(head):
    """
    删除链表中子链表和为0的子链表
    :param head:
    :return:
    """
    # if not head or not head.next:
    #     return head
    ###利用前缀和来保存该节点和他的next节点，如果两个节点的前缀和相等则两个节点的和为0
    mapping = {}
    dummy = ListNode(0)
    dummy.next = head
    preix = 0
    mapping[preix] = dummy
    while head:
        preix += head.val
        mapping[preix] = head
        head = head.next

    head = dummy
    preix = 0
    while head:
        preix += head.val
        head.next = mapping[preix].next
        head = head.next
    return dummy.next