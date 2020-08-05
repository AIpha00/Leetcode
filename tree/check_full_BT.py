# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""

"""
判断一颗树是否是满二叉树

"""
from tree.base_tree_train import TreeNode


def solution(root):
    """
    判断一棵树是否是满二叉树，DFS
    :param root:
    :return:
    """
    all_layer = {}

    def DFS(layer, root):
        if not root:
            return
        all_layer[layer] = all_layer.get(layer, 0) + 1
        if root.left:
            DFS(layer + 1, root.left)
        if root.right:
            DFS(layer + 1, root.right)

    DFS(0, root)

    for i, val in all_layer.items():
        if 2 ** i != val:
            return False
    return True


if __name__ == '__main__':
    tree = TreeNode()
    node = [1, 2, 3, 4, 5, 6, 7]
    for i in node:
        tree.add(i)

    print(solution(tree.root))
    # print(all_layer)
