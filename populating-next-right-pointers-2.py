# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    # Refer to http://chaoren.is-programmer.com/posts/43820.html
    def connect(self, root):
        curr = root
        #traverse level by level
        while curr:
            next_level_start = None
            prev = None
            #traverse through the current level
            while curr:
                #get the starting node of the next level
                if not next_level_start:
                    next_level_start = curr.left if curr.left else curr.right
                #populating, from left to right
                if curr.left:
                    if prev:
                        prev.next = curr.left
                    prev = curr.left
                if curr.right:
                    if prev:
                        prev.next = curr.right
                    prev = curr.right
                #to the next node of the same level
                #note that next of this level has already been populated when processing it's above level
                curr = curr.next
            #to the first node of the next level
            curr = next_level_start
