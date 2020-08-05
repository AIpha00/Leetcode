# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""
"""
判断是否是一颗对称二叉树
"""
from tree.base_tree_train import TreeNode


def isSymmetric(root):
    """
    判断是否是一颗对称二叉树
    :param self:
    :param root:
    :return:
    """
    if not root: return False
    res_front = []
    res_later = []
    front_sort(root, res_front)
    later_sort(root, res_later)
    if res_front == res_later[::-1]:
        return True
    return False


def helper(left, right):
    """
    通过对比二叉树的左右子树来判断是否对称！！
    :param left:
    :param right:
    :return:
    """
    if not left and not right:
        return True
    if not left or not right:
        return False
    if left.val != right.val:
        return False
    return helper(left.left, right.right) and helper(left.right, right.left)



def front_sort(root, res):
    """
    前序遍历， 根节点-->左子树-->右子树
    :param root:
    :param res:
    :return:
    """
    if not root:
        return
    res.append(root.val)
    front_sort(root.left, res)
    front_sort(root.right, res)


def later_sort(root, res):
    """
    后序遍历， 左子树-->右节点-->根节点
    :param root:
    :param res:
    :return:
    """
    if not root:
        return
    later_sort(root.left, res)
    later_sort(root.right, res)
    res.append(root.val)


if __name__ == '__main__':
    TreeNode = TreeNode()
    for val in range(10):
        TreeNode.add(val)
    print(isSymmetric(TreeNode.root))
