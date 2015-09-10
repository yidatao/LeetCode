# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        return self.sum(root, 0)

    #TODO need to revisit
    def sum(self, node, curSum):
        if node is None:
            return 0
        #parent's value * 10 + node's value is the number
        curSum = curSum * 10 + node.val
        if node.left is None and node.right is None:
            #when reaching leaf, return the number that is constructed by root to this leaf
            return curSum
        return self.sum(node.left, curSum) + self.sum(node.right, curSum)
