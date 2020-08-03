# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""

"""
判断在二叉树中是否存在一条一直向下的路径，使得每个节点的值恰好一一对应以head为首的链表中的值

leetcode: 1367
"""

from LeetCode.common.ListNode import ListNode
from LeetCode.tree.base_tree_train import TreeNode


def isSubPath(head, root):
    """
    判断是否存在一个子链表可以对应二叉树中的一条纵向路径
    :param head:
    :param root:
    :return:
    """
    if not head or not root:
        return False
    stack = [root]
    listnode = [head]
    queue = [root]
    while queue and stack:

        node = stack.pop()
        lnode = listnode.pop()
        if not lnode.next:
            break
        # check_node = queue.pop(0)
        for check_node in queue:
            if check_node.elem == lnode.val:
                listnode.append(lnode.next)
                break
            else:
                listnode.append(lnode)
        queue = []
        if node.rchild:
            stack.append(node.rchild)
            queue.append(node.rchild)
        if node.lchild:
            stack.append(node.lchild)
            queue.append(node.lchild)
    if listnode:
        return False
    return True


"""
讨论区答案
"""

"""
就应该先使用递归！多谢递归版的解题答案
"""


def dfs(head, root):
    if not head:
        return True
    if not root:
        return False
    if root.val != head.val:
        return False
    ##深度优先遍历，链表节点和左右子树节点依次比较，返回
    if dfs(head.next, root.left) or dfs(head.next, root.right):
        return True
    return False


def isSubPath_answer(head: ListNode, root: TreeNode) -> bool:
    if not root:
        return False
    if dfs(head, root):
        return True
    return isSubPath_answer(head, root.left) or isSubPath_answer(head, root.right)


if __name__ == '__main__':
    tree = TreeNode()
    treeNode = [1, 4, 5, 8, 1, None, None, 4, None, None, 9]
    for i in treeNode:
        tree.add(i)

    head = ListNode(4, next=ListNode(1, next=None))
    # headnode = [4,2,8]
    # while headnode:
    #     head.next = ListNode(headnode.pop(0))
    #
    print(isSubPath(head, tree.root))
