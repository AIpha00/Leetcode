# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""

"""
删除链表末尾的第n个节点，并返回
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNode(head, n):
    def find(node):
        if not node:
            return 0

        i = find(node.next) + 1
        if i > n:
            node.next.val = node.val
        return i

    find(head)
    return head.next
    pass


res_lis = []


def printNode(node):
    while node.next:
        print(node.val, '-->', end='')
        # return node.val
        node = node.next
    print(node.val, end='\n')
    # res_lis.append(node.val)
    # node = node.next
    # printNode(node)


if __name__ == '__main__':
    head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
    printNode(head)
    res = removeNode(head, 1)
    printNode(res)
