# -*- coding: utf-8 -*-
"""
 author: NotOne
 data:2020-08-11 11:39
"""

"""
将单链表所有的奇偶节点分开排在一起,这里的奇偶是指节点编号的奇偶性，不是节点的值的奇偶性
leetcode:328
"""
from common.ListNode import ListNode, buildNode, printNode


def oddEvenList(head):
    """
    将链表的奇偶节点分开
    :param head:
    :return:
    """
    if not head:
        return head

    #记录编号为奇数的节点
    odd = head  ##用head来做头节点
    #记录编号为偶数的节点
    even_head = even = head.next
    while odd.next and even.next:
        #将节点的下个节点指向每步走两个节点
        odd.next = odd.next.next
        even.next = even.next.next

        ##把当前节点更新为下一个节点
        odd, even = odd.next, even.next

    odd.next = even_head
    return head







    # odd, even = ListNode(0), ListNode(0)
    # cur_odd = odd
    # cur_even = even
    # cur = head
    # while head:
    #     if head.val & 1 == 1:
    #         odd.next = head
    #         cur.next = None
    #         head = head.next
    #         odd = odd.next
    #     if head.val & 1 == 0:
    #         even.next = head
    #         cur.next = None
    #         cur = cur.next
    #         head = head.next
    # odd.next = cur_even.next
    # return odd
    # odd = head
    # even_head = even = head.next
    # while odd.next and even.next:
    #     odd.next = odd.next.next
    #     even.next = even.next.next
    #     odd, even = odd.next, even.next
    # odd.next = even_head
    # return head





if __name__ == '__main__':
    vals = [1, 2, 3, 4, 5]
    listnode = buildNode(vals)
    res = oddEvenList(listnode)
    printNode(res)