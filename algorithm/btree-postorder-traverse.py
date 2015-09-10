class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        result = []
        list = []
        visited_node = None
        cur_node = root
        while len(list) > 0 or cur_node is not None:
            if cur_node is not None:
                list.append(cur_node)
                cur_node = cur_node.left
            else:
                middle_node = list[len(list)-1]
                #visit the middle node only if the right node is none, or the right node is already visited
                if middle_node.right is None or visited_node == middle_node.right:
                    #visit the middle node
                    result.append(middle_node.val)
                    visited_node = list.pop(len(list)-1)
                else:
                    #else, move to right
                    cur_node = middle_node.right
        return result
