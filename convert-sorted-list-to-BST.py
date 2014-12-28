# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        array = []
        while head is not None:
            array.append(head.val)
            head = head.next
        if len(array) == 0:
            return None
        return self.buildTree(array, 0, len(array)-1)

    def buildTree(self, array, start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        node = TreeNode(array[mid])
        node.left = self.buildTree(array, start, mid-1)
        node.right = self.buildTree(array, mid+1, end)
        return node