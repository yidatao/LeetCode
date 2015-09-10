# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        #globale variable for the globally max sum
        self.maxVal = float("-inf")
        self.maxSum(root)
        return self.maxVal

    #this function computes the max path sum for the node's subtree
    #Unlike the definition of this problem, the path eligible for this function should contain node as the **ending point**
    #so that after the recursion returns, we can use node as the connecting node to form another path
    def maxSum(self, node):
        if node is None:
            return 0
        leftMaxSum = self.maxSum(node.left)
        rightMaxSum = self.maxSum(node.right)
        #update the global max path sum
        self.maxVal = max(self.maxVal, node.val, node.val + leftMaxSum, node.val + rightMaxSum, node.val + leftMaxSum + rightMaxSum)
        #to form a path, we need the node to be the connecting dot, i.e., the end of the path should always be this node
        #for this reason, the below line doesn't contain node.val + leftMaxSum + rightMaxSum, in which node isn't the ending point
        #but node.val + leftMaxSum + rightMaxSum should be considered when computing the global max path sum in the above line
        return max(node.val, node.val + leftMaxSum, node.val + rightMaxSum)

a = TreeNode(0)
# a.left = TreeNode(2)
# a.right = TreeNode(3)
print(Solution().maxPathSum(a))
