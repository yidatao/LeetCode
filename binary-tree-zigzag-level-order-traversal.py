# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if root is None: return []
        res = []
        curlevel = [root]
        leftToRight = True
        while len(curlevel) > 0:
            level = []
            next_level = []
            while len(curlevel) > 0:
                #from the last node
                node = curlevel.pop()
                level.append(node.val)
                if leftToRight:
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                else:
                    if node.right:
                        next_level.append(node.right)
                    if node.left:
                        next_level.append(node.left)
            res.append(level)
            curlevel = next_level
            leftToRight = not leftToRight
        return res