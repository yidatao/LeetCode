# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    stack = []

    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.inorder(root)

    def inorder(self, node):
        if node is None: return
        self.inorder(node.left)
        self.stack.insert(0, node.val)
        self.inorder(node.right)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return True if len(self.stack) > 0 else False

    # @return an integer, the next smallest number
    def next(self):
        return self.stack.pop()
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())