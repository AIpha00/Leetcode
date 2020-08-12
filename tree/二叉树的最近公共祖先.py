# -*- coding: utf-8 -*-
"""
 author: NotOne
 data:2020-08-10 16:37
"""

"""
给定二叉树的两个节点，返回二叉树中这两个节点的最近公共祖先
leetcode: 236
"""

from tree.base_tree_train import TreeNode, Node


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        给定两个节点p,q和一棵二叉树，返回这两个节点的最近公共祖先

        从一个节点出发，看p,q在那个节点分开，即，这个从这个节点出发，左节点和右节点分别找到了p或者q
        :param root:
        :param p:
        :param q:
        :return:
        """
        """
        递归模版
        """
        # print('jinru.')
        ##终止条件
        if not root:
            return root
        if root.val == p.val or root.val == q.val:
            return root

        ##在这一层需要做什么
        # 什么也不做

        ##分别递归左树和右树
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        ##回到这一层需要做什么
        ##在这一层需要判断，有没有在当前节点找到p和q
        if not left:
            return right
        if not right:
            return left

        ##左节点和右节点都存在，说明当前节点就是最近公共祖先
        return root


if __name__ == '__main__':
    tree = TreeNode()
    node = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    for n in node:
        tree.add(n)
    p = Node(5)
    q = Node(1)
    S = Solution()
    res = S.lowestCommonAncestor(tree.root, p, q)
    print(res.val)
