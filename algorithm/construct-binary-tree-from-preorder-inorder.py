# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    # Memory limit exceeded
    def buildTree0(self, preorder, inorder):
        #finishing condition
        if len(preorder) == 0: return None
        root = TreeNode(preorder[0])
        #use inorder to decide left and right size
        index = inorder.index(root.val)
        #recursion
        root.left = self.buildTree(preorder[1:1+index],inorder[:index])
        root.right = self.buildTree(preorder[1+index:], inorder[index+1:])
        return root

    def buildTree(self, preorder, inorder):
        return self.build(preorder, inorder, 0, 0, len(inorder)-1)

    #pass preorder and inorder instead of creating new list
    #ind_pre: the starting index of preorder list
    #ind_inorder_start, ind_inorder_end: the starting and ending index of inorder list
    #these indices are relative to the original preorder, inorder lists
    def build(self, preorder, inorder, ind_pre, ind_inorder_start, ind_inorder_end):
        if ind_inorder_start > ind_inorder_end: return None
        root = TreeNode(preorder[ind_pre])
        #the questions says there is no duplicate, so we can directly find index of the root in inorder list
        ind = inorder.index(root.val)
        root.left = self.build(preorder, inorder, ind_pre + 1, ind_inorder_start, ind - 1)
        root.right = self.build(preorder, inorder, ind_pre + (ind - ind_inorder_start) + 1, ind+1, ind_inorder_end)
        return root

