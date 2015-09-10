class Solution:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        if root is None:
            return []
        res = []
        queue = [root]
        while queue:
            #size of the current level
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                #only add the right-most node of the current level
                if i == 0:
                    res.append(node.val)
                #current level starts from the right-most node
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return res