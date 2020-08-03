# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""

"""
平衡二叉树的概念：
任何一个结点的左子树和右子树都是平衡二叉树，并且高度之差的绝对值不超过1
"""

"""
判断一颗树是否是平衡二叉树的解题思路：
求出该二叉树的深度
"""
from LeetCode.tree.base_tree_train import TreeNode


def tree_depth(root):
    """
    求出二叉树的深度
    :param root:
    :return:
    """
    if not root:
        return 0
    left = tree_depth(root.left)
    right = tree_depth(root.right)
    return max(left, right) + 1


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.flag = True
        self.balance_tree_depth(root)
        return self.flag

    def balance_tree_depth(self, root):
        if not root or not self.flag:
            return 0
        left_length = self.balance_tree_depth(root.left)
        right_length = self.balance_tree_depth(root.right)
        if abs(left_length - right_length) > 1:
            self.flag = False
        return max(left_length, right_length) + 1


if __name__ == '__main__':
    tree_list = range(4)
    tree = TreeNode()
    for i in range(4):
        tree.add(i)
    # print(tree_depth(tree.root))
    print(Solution().isBalanced(tree.root))
