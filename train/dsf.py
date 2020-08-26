# -*- coding: utf-8 -*-
"""
 author: NotOne
 data:2020-08-19 14:39
"""

"""
记忆加默写深度优先搜索的递归写法和非递归写法
"""
from tree.base_tree_train import TreeNode


def dfs(res, root):
    """
    递归写法
    :param root:
    :return:
    """
    if not root:
        return
    print(root.val)
    res.append(root.val)
    if root.left:
        dfs(res, root.left)

    if root.right:
        dfs(res, root.right)
    return res, root


def Fdfs(root):
    """
    深度优先遍历非递归版
    :param root:
    :return:
    """
    if not root:
        return
    res = []
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res


def layer(root):
    """
    层序遍历
    :param root:
    :return:
    """
    if not root:
        return
    res = []
    queue = [root]
    while queue:
        layer_res = []
        for i in range(len(queue)):
            node = queue.pop(0)
            layer_res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if layer_res:
            res.append(layer_res)
    return res


"""
前中后序遍历
"""


def preorder(res, root):
    """
    前序遍历
    :param root:
    :return:
    """
    #递归终止条件
    if not root:
        return

    ##在这一层做什么
    print(root.val)
    if root.left:
        preorder(res, root.left)
    if root.right:
        preorder(res, root.right)
    ##回到这一层做什么
    return res, root

if __name__ == '__main__':
    tree = TreeNode()
    node_lis = [1, 2, 3, 4, 5, 6]
    for node in node_lis:
        tree.add(node)
    res = []
    res, root = dfs(res, tree.root)
    print('默写:', res)
    Fres = Fdfs(tree.root)
    print('默写非递归版', Fres)
    res_f = tree.DFS(tree.root)
    print('非默写:', res_f)
    print('')
    res_l = layer(tree.root)
    print('默写层序遍历:', res_l)
    res_fl = tree.layer_traverse(tree.root)
    print('非默写层序遍历:', res_fl)

    pre_res, _ = preorder([], tree.root)
    print(pre_res)