# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""

"""
实现链表的翻转，递归和非递归
"""
from LeetCode.common.ListNode import ListNode, printNode

cur = last = ListNode(0)  ## 新链表头，和当前替换的结点


def reverseList(node):
    """
    翻转链表递归版
    :param node:
    :return:
    """

    if not node.next:
        return node

    last_node = reverseList(node.next)
    last_node.next = node
    node.next = None
    global cur
    cur.next = last_node
    # last = last.next
    cur = last_node
    return cur.next


def reverse_List(head):
    """
    反转单向链表， 1 -> 2 -> 3 -> 4
    1. 4 -> 3 -> None
            ^
    1 -> 2 /
    2. 4 -> 3 -> 2 -> None
                ^
            1 /
    3. 4 -> 3 -> 2 -> 1 -> None
    :param head:
    :return:
    """
    if not head.next:
        return head
    last = reverse_List(head.next)  ###last就是一个崭新的链表头
    head.next.next = head  ##head.next.next 作为替换节点
    head.next = None
    return last


def reverseListByN(head, n):
    if n == 1:
        return head
    last = reverseListByN(head.next, n - 1)
    head.next.next = head
    head.next = None
    return last


if __name__ == '__main__':
    node = ListNode(0, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5)))))
    print("原链表：")
    printNode(node)
    re_node = reverseListByN(node, 4)
    print('反转链表：')
    printNode(re_node)
