# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""

"""
二叉树的层次遍历
"""
from tree.base_tree_train import TreeNode


def levelOrder(root):
    """
    二叉树的层次遍历，使用宽度优先遍历实现
    :param root:
    :return:
    """
    if not root:
        return []
    res = []
    queue = []
    queue.append(root)

    ##visited 标记已经
    # visited = set()

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):  ##直接遍历队列也行
            node = queue.pop(0)
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(current_level)
    return res


res_dict = {}


def levelOrderByDFS(root):
    """
    使用深度优先遍历，实现层次遍历
    :param root:
    :return:
    """
    level = 0
    helper(level, root)
    pass


def helper(level, root):
    """
    深度优先遍历帮助函数
    :param root:
    :return:
    """
    if not root:
        return
    if level not in res_dict:
        res_dict[level] = []
    res_dict[level].append(root.val)

    helper(level + 1, root.left)
    helper(level + 1, root.right)
    pass


if __name__ == '__main__':
    node = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tree = TreeNode()
    for i in node:
        tree.add(i)

    res = levelOrderByDFS(tree.root)
    print(res_dict)
