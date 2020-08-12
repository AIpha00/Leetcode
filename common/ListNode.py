# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""
"""
链表的公共文件，存储
"""


class ListNode():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def buildNode(vals):
    head = cur = ListNode(0)
    for val in vals:
        lis = ListNode(val)
        cur.next = lis
        cur = cur.next
    return head.next
        

def printNode(node):
    while node.next:
        print(node.val, '--> ', end='')
        # return node.val
        node = node.next
    print(node.val, end='\n')
