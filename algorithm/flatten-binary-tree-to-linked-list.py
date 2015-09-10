# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten0(self, root):
        res = []
        self.preorder(root, res)
        node = root
        for v in res[1:]:
            node.left = None
            node.right = TreeNode(v)
            node = node.right


    def preorder(self, node, res):
        if node is None:
            return
        res.append(node.val)
        self.preorder(node.left, res)
        self.preorder(node.right, res)

    def flatten(self, root):
        if root is None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left is None:
            #already done
            return
        node = root.left
        while node.right:
            node = node.right
        #append left subtree before right subtree
        node.right = root.right
        root.right = root.left
        root.left = None
