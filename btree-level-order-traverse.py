class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root is None:
            return []
        result = []
        cur_level = [root]
        #basically in a BFS manner, level by level
        while len(cur_level) > 0:
            level = []
            next_level = []
            for node in cur_level:
                level.append(node.val)
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            result.append(level) #if the result is bottom-up, then simply insert each level to the beginning: result.insert(0,level)
            cur_level = next_level
        return result