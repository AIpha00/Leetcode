# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""

"""
验证二叉树是否为二叉搜索树
leetcode: 98
"""

"""
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
"""

"""

"""

from LeetCode.tree.base_tree_train import TreeNode

"""
解法1：
利用中序遍历，判断结果是否是一个升序的列表
"""
"""
解法2：
递归，找到左子树的max 右子树的min，使得 max < root < min
"""


class Solution:
    """
    使用中序遍历判断当前节点的值是否大于上一个节点的值
    """

    def isValidBST(self, root: TreeNode) -> bool:
        self.prev = None
        return self.helper(root)

    def helper(self, root):
        if not root:
            return True
        ####访问左子树，判断当前节点的left是否存在，若不存在返回false
        if not self.helper(root.left):
            return False
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        return self.helper(root.right)
