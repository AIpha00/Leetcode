# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""

"""
将二叉树搜索树转换成单向链表，即将二叉树的左节点置为null，值为右节点、在原址上进行操作
Leetcode: 面试题17.12
"""
from LeetCode.tree.base_tree_train import TreeNode


class Solution:
    def convertBiNode(self, root):
        """
        将二叉搜索树转换为链表
        :param root:
        :return:
        """
        # self.queue = []
        self.prev = self.start = TreeNode().root
        self.helper(root)
        # head = TreeNode()
        # head.add(0)
        # node = self.queue.pop(0)
        # head.root.right = node
        # while self.queue:
        #     node.right = self.queue.pop(0)
        #     node = node.right

        return self.start.right

    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        # self.queue.append(root)
        self.prev.left = None
        self.prev.right = root
        self.prev = root
        self.helper(root.right)


if __name__ == '__main__':
    S = Solution()
    tree = TreeNode()
    node = [4, 2, 5, 1, 3, None, 6, 0]
    for i in node:
        tree.add(i)
    new_tree = S.convertBiNode(tree.root)
    # print(new_tree)
    print(tree.layer_traverse(new_tree))