# -*- coding: utf-8 -*-
"""
 author: NotOne
 data:2020-08-20 11:02
"""
from tree.base_tree_train import TreeNode


def invertTree(root):
    if not root:
        return
    node = root.left
    root.left = root.right
    root.right = node
    invertTree(root.left)
    invertTree(root.right)
    return root


if __name__ == '__main__':
    node_lis = [4, 2, 7, 1, 3, 6, 9]
    tree = TreeNode()
    for node in node_lis:
        tree.add(node)
    res = invertTree(tree.root)
    print(tree.layer_traverse(res))