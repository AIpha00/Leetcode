# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""

"""
基础二叉树训练，熟悉二叉树的数据结构和基础的遍历方法
"""


class Node(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeNode(object):
    def __init__(self):
        self.root = Node()
        self.myQueue = []  ## 用队列来保存左右节点

    def add(self, val):
        """
        为树添加节点
        :param val:
        :return:
        """
        node = Node(val)
        if self.root.val == None:  ##判断树是否为空，如果为空则对根节点赋值
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]
            if treeNode.left == None:
                treeNode.left = node
                self.myQueue.append(treeNode.left)
            else:
                treeNode.right = node
                self.myQueue.append(treeNode.right)
                self.myQueue.pop(0)  ##如果该节点存在右子树，将此节点丢弃,将这个右节点的根节点移除节点队列

    def front_recursive(self, root):
        """
        二叉树的前序遍历
        :return:
        """
        """
        根节点-->左子树-->右子树
        """
        if root == None:
            return
        print(root.val, end='')
        self.front_recursive(root.left)
        self.front_recursive(root.right)

    def middle_recursive(self, root):
        """
        中序遍历
        :param root:
        :return:
        """
        """
        左子树-->根节点-->右子树
        """
        if root == None:
            return
        self.middle_recursive(root.left)
        print(root.val, end='')
        self.middle_recursive(root.right)

    def later_recursive(self, root):
        """
        后序遍历
        :param root:
        :return:
        """
        """
        左子树-->右子树-->根节点
        """
        if root == None:
            return
        self.later_recursive(root.left)
        self.later_recursive(root.right)
        print(root.val, end='')

    """
    非递归版遍历
    """

    def front_stack(self, root):
        """
        非递归版的前序遍历
        :param root:
        :return:
        """
        """
        while 左子树的左叶子节点
        """
        if not root: return
        Stack = []
        node = root
        while node or Stack:
            while node:
                print(node.val, end='')
                Stack.append(node)
                node = node.left
            node = Stack.pop()
            node = node.right

    def middle_stack(self, root):
        """
        非递归版的中序遍历， 左中右
        :param root:
        :return:
        """
        if not root: return
        Stack = []
        node = root
        while node or Stack:
            ##先找到左节点
            while node:
                ##入栈的是左节点的父节点
                Stack.append(node)
                node = node.left
            node = Stack.pop()
            print(node.val, end='')
            node = node.right

    def later_stack(self, root):
        if not root: return
        R_Stack, L_Stack = [], []
        node = root
        L_Stack.append(node)
        while L_Stack:
            node = L_Stack.pop()
            if node.left:
                L_Stack.append(node.left)
            if node.right:
                L_Stack.append(node.right)
            R_Stack.append(node)
        while R_Stack:
            node = R_Stack.pop()
            print(node.val, end='')
            pass

    def layer_traverse(self, root):
        """
        利用队列实现二叉树的层级遍历， 也就是广度优先遍历
        :param root:
        :return:
        """
        if not root: return
        queue = []  ### 队列用来存储每一层的所有节点
        node = root
        queue.append(node)
        res = []
        while queue:
            layer_list = []
            # print(node.val, end='')
            for i in range(len(queue)):
                node = queue.pop(0)
                layer_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if layer_list:
                res.append(layer_list)
        return res

    def DFS(self, root):
        """
        深度优先遍历
        :param root:
        :return:
        """
        """
        从根节点出发，沿着左子树纵向遍历，知道找到叶子节点为止，然后回溯到前一个节点，进行右子树节点的遍历，知道遍历完所有可达节点为止
        """
        if not root: return
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res


if __name__ == '__main__':
    first_tree = TreeNode()
    for val in range(1, 9):
        first_tree.add(val)

    root = first_tree.root
    print('前序遍历:', end='')
    first_tree.front_recursive(root)
    print('\n中序遍历:', end='')
    first_tree.middle_recursive(root)
    print('\n后序遍历:', end='')
    first_tree.later_recursive(root)

    print('\n前序遍历-非递归版:', end='')
    first_tree.front_stack(root)
    print('\n中序遍历-非递归版:', end='')
    first_tree.middle_stack(root)
    print('\n后序遍历-非递归版:', end='')
    first_tree.later_stack(root)

    print('\n层次遍历:', end='')
    print(first_tree.layer_traverse(root))

    print('\n深度优先遍历:', end='')
    print(first_tree.DFS(root))
