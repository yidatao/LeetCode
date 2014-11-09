# Definition for a  binary tree node
class Node:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    x=''
    # @param root, a tree node
    # @return a boolean
    def isSymmetric0(self, root):
        if root is None:
            return True
        self.inorder(root)
        print(self.x)
        return self.x == self.x[::-1]
    #inorder alone cannot define a tree. Must be (in-order+pre-order) or (in-order+post-order) can determine a tree uniquely
    def inorder(self, node):
        if node is None:
            self.x += '#'
            return
        self.inorder(node.left)
        self.x += str(node.val)
        self.inorder(node.right)

    def isSymmetric1(self, root):
        if root is None:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
        return root1.val == root2.val and self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)


t = Node(1, Node(2,Node(3)),Node(3, Node(2)))
print(Solution().isSymmetric1(t))