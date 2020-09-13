# -*- coding: utf-8 -*-
"""
 author: NotOne
 data:2020-08-11 16:07
"""

"""
找到有序链表中的中位数

双指针，快慢指针，快指针走到头，慢指针恰好在中间，因为fast == 2 * slow
"""
from common.ListNode import buildNode
from tree.base_tree_train import Node


def findMidList(head):
    """
    找到有序链表的中间值
    :param head: 
    :return: 
    """
    if not head:
        return head
    slow, fast = head, head
    while fast.next and slow.next:
        cur = slow
        slow = slow.next
        fast = fast.next.next
    if cur:
        cur.next = None
    return slow


def DFS(head):
    if not head:
        return None

    mid = findMidList(head)

    node = Node(mid.val)

    if head == mid:
        return node

    node.left = DFS(head)
    node.right = DFS(mid.next)

    return node


if __name__ == '__main__':
    a = [4, 2, 1, 3, 8]
    head = buildNode(a)
    # res = DFS(head)
    res = findMidList(head)
    # res_0 = findMidList(res.next)
    # res_1 = findMidList(res_0.next)
    print(res)
