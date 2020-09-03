# -*- coding: utf-8 -*-
"""
 author: NotOne
 data:2020-09-01 11:49
"""
from tree.base_tree_train import TreeNode, Node


def layers(root):
    if not root:
        return root
    queue = [root]
    res = []
    while queue:
        node = queue.pop(0)
        if node and node.val != None:
            res.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append('null')
    return '[' + ','.join(res) + ']'


def deserialize(data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    if not data:
        return None
    nodeList = data[1:-1].split(',')
    # treeQueue = []
    i = 1
    rootHead = Node(int(nodeList[0]))
    queue = [rootHead]
    while i < len(nodeList):
        root = queue[0]
        if nodeList[i] != 'null':
            root.left = Node(int(nodeList[i]))
            queue.append(root.left)
        i += 1
        if nodeList[i] != 'null':
            root.right = Node(int(nodeList[i]))
            queue.append(root.right)
        queue.pop(0)
        i += 1
    return rootHead


    # root = Node('#')
    # for val in nodeList:
    #     if root.val == '#':
    #         if val != 'null':
    #             node = Node(int(val))
    #             root = node
    #             treeQueue.append(root)
    #             continue
    #     treeRoot = treeQueue[0]
    #     if treeRoot.left is None:
    #         if val != 'null':
    #             node = Node(int(val))
    #             treeRoot.left = node
    #             treeQueue.append(treeRoot.left)
    #     elif treeRoot.right is None:
    #         if val != 'null':
    #             node = Node(int(val))
    #             treeRoot.right = node
    #             treeQueue.append(treeRoot.right)
    #             treeQueue.pop(0)
    # return root


if __name__ == '__main__':
    tree = TreeNode()
    nodeList = [1, 2, 3, None, None, 4, 5]
    for node in nodeList:
        tree.add(node)
    res = layers(tree.root)
    print(res)
    resTree = deserialize(res)
    layerRes = tree.layer_traverse(resTree)
    print(layerRes)
