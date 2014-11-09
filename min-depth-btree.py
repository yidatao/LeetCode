class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        elif root.left is None:
            return 1 + self.minDepth(root.right)
        elif root.right is None:
            return 1 + self.minDepth(root.left)

        return 1 + min(self.minDepth(root.left),self.minDepth(root.right))

    def depth(self, node):
        if node is None:
            return 0
        return 1 + max(self.depth(node.left), self.depth(node.right))