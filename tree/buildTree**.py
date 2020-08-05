# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""
"""
根据前序遍历和后序遍历，重新将二叉树进行构建
Leetcode: 剑值offer 07
"""
from tree.base_tree_train import TreeNode, Node


class Solution:
    def buildTree(self, preorder, inorder):
        """
        根据前序遍历和中序遍历重新构建出这颗二叉树
        :param preorder:
        :param inorder:
        :return:
        """
        pass
        new_tree = TreeNode()

        mapping = {}
        for idx, val in enumerate(inorder):
            if val not in mapping:
                mapping[val] = None
            mapping[val] = idx
        size = len(preorder)
        stack = []
        queue = []
        is_back = False
        for i in range(size - 1):
            if not stack:
                is_back = False
            if new_tree.root.val == None:
                root = Node(preorder[i])
                new_tree.root = root
                queue.append(root)
            if mapping[preorder[i]] != 0 and not is_back:
                root = queue.pop(0)
                stack.append(root)
            else:
                is_back = True

            # else:
            if is_back:
                root = stack.pop()
            if not stack:
                is_back = False
                queue = []

            # else:
            if mapping[preorder[i]] < mapping[preorder[i + 1]]:
                root.right = Node(preorder[i + 1])
                if not is_back:
                    queue.append(root.right)
            if mapping[preorder[i]] > mapping[preorder[i + 1]]:
                root.left = Node(preorder[i + 1])
                if not is_back:
                    queue.append(root.left)
                pass

        return new_tree

    def buildTreeByBook(self, preorder, inorder):
        """
        来自《python程序面试宝典》7.4.3
        :param preorder:
        :param inorder:
        :return:
        """
        self.nodeMap = {}
        self.root = None

        for idx, val in enumerate(inorder):
            self.nodeMap[val] = idx
        self.buildTreeByBookHelper(preorder)
        return self.root

    def buildTreeByBookHelper(self, preorder):
        """
        通过中序遍历判断结点位置
        :param inorder:
        :return:
        """
        if self.root == None:
            self.root = Node(preorder[0])

        for i in range(1, len(preorder)):
            val = preorder[i]
            current = self.root

            while True:
                if self.nodeMap[val] < self.nodeMap[current.val]:
                    if current.left is not None:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                else:
                    if current.right is not None:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break

        # return self.root

    def buildTreeByLeetcodeAnswer(self, preorder, inorder) -> TreeNode:
        self.dic, self.po = {}, preorder
        for i in range(len(inorder)):
            self.dic[inorder[i]] = i
        return self.recur(0, 0, len(inorder) - 1)

    def recur(self, pre_root, in_left, in_right):
        if in_left > in_right: return  # 终止条件：中序遍历为空
        root = TreeNode(self.po[pre_root])  # 建立当前子树的根节点
        i = self.dic[self.po[pre_root]]  # 搜索根节点在中序遍历中的索引，从而可对根节点、左子树、右子树完成划分。
        root.left = self.recur(pre_root + 1, in_left, i - 1)  # 开启左子树的下层递归
        root.right = self.recur(i - in_left + pre_root + 1, i + 1, in_right)  # 开启右子树的下层递归
        return root  # 返回根节点，作为上层递归的左（右）子节点

        # pass


if __name__ == '__main__':
    preorder = [6, 4, 2, 1, 3, 5, 9, 7, 8, 10]
    inorder = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    S = Solution()
    new_tree = S.buildTreeByBook(preorder, inorder)

    print(new_tree)
