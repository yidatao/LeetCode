class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        result = []
        list = []
        cur_node = root
        while len(list)>0 or cur_node is not None:
            if cur_node is not None:
                #push the middle node to stack
                list.append(cur_node)
                cur_node = cur_node.left
            else:
                node = list.pop(len(list)-1)
                result.append(node.val)
                cur_node = node.right
        return result