class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        return self.generateT(1, n)

    def generateT(self, start, end):
        if start > end: return [None]
        res = []
        for i in range(start, end+1):
            ll = self.generateT(start, i-1)
            rl = self.generateT(i+1, end)
            for l in ll:
                for r in rl:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res


print(Solution().generateTrees(6))