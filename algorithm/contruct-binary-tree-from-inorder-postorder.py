# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        return self.build(inorder, postorder, 0, len(inorder)-1, 0, len(postorder)-1)

    def build(self, inorder, postorder, inorder_start, inorder_end, postorder_start, postorder_end):
        if inorder_start > inorder_end: return None
        root = TreeNode(postorder[postorder_end])
        ind = inorder.index(root.val)
        root.left = self.build(inorder, postorder, inorder_start, ind - 1, postorder_start, postorder_start + ind - inorder_start - 1)
        root.right = self.build(inorder, postorder, ind + 1, inorder_end, postorder_start + ind - inorder_start, postorder_end - 1)
        return root