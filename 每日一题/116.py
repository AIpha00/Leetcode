# -*- coding: utf-8 -*-
# @Time : 2020/10/15
# @Author : NotOne


"""
leetcode: 116
填充他的每个指针
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        ## 一次层序遍历
        Queue = [root]
        while Queue:
            size = len(Queue)
            for i in range(size):
                node = Queue.pop(0)
                ## 这里连接下一个节点 需要判断i是否有效，以及将队列首端弹出后，第一个既是下一个
                if i < size - 1:
                    node.next = Queue[0]
                if node.left:
                    Queue.append(node.left)
                if node.right:
                    Queue.append(node.right)
        return root
