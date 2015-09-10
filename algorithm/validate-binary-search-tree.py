# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.isValid(root, float("-inf"), float("inf"))

    #This is one brilliant solution, by http://stackoverflow.com/questions/499995/how-do-you-validate-a-binary-search-tree
    def isValid(self, node, MIN, MAX):
        if node is None:
            return True
        if node.val > MIN and node.val < MAX and self.isValid(node.left, MIN, node.val) and self.isValid(node.right, node.val, MAX):
            return True
        return False
