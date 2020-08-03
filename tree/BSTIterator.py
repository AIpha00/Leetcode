# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""

"""
实现一个二叉搜索树迭代器

leetcode: 173
"""
from LeetCode.tree.base_tree_train import TreeNode

"""
二叉搜索树: 若左子树不空，则左子树上所有节点的值均小于它的根节点的值；若它的右节点不空，则右子树上的所有节点的值均大于它的根节点的值， 示例：
      7
    3   15
       9   20
"""


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.root = root
        self.stack = []
        self.sort_tree(root)

    def next(self):
        """
        返回下一个最小的数
        :return:
        """
        return self.stack.pop()

    def hasnext(self):
        """
        返回是否还存在下一个最小的树
        :return:
        """
        if len(self.stack):
            return True
        return False

    def sort_tree(self, root):
        """
        对二叉树进行排序
        :return:
        """
        if not root:
            return
        self.sort_tree(root.left)
        if root.val:
            self.stack.append(root.val)
        self.sort_tree(root.right)


if __name__ == '__main__':
    node_list = [7, 3, 15, None, None, 9, 20]
    tree = TreeNode()
    for val in node_list:
        tree.add(val)

    iterator = BSTIterator(tree.root)
    # print(iterator.next())
    print(iterator.stack)
