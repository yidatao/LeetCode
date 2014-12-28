# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree0(self, root):
        self.val_list = []
        self.node_list = []
        self.inOrder(root)
        #sort the values
        self.val_list = sorted(self.val_list)
        for i in range(len(self.val_list)):
            #the re-assign to nodes the sorted values
            self.node_list[i].val = self.val_list[i]
        return root

    #In-order traverse is commonly used on BST
    #since the traverse returns sorted values already
    def inOrder(self, node):
        if node is None:
            return
        self.inOrder(node.left)
        self.val_list.append(node.val)
        self.node_list.append(node)
        self.inOrder(node.right)

    def recoverTree(self, root):
        #two misplaced nodes
        self.node1 = None
        self.node2 = None

        #the previous node to the current node (by in order)
        self.prev = None

        self.inOrderTraverse(root)
        #swap values
        self.node1.val, self.node2.val = self.node2.val, self.node1.val

        return root

    def inOrderTraverse(self, node):
        if node is None:
            return
        self.inOrderTraverse(node.left)
        if self.prev is not None:
            #if it violates BST
            if self.prev.val >= node.val:
                #if node1 hasn't been found
                if self.node1 is None:
                    self.node1 = self.prev
                self.node2 = node
        self.prev = node
        self.inOrderTraverse(node.right)