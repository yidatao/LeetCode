class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        result = []
        list = []
        cur_node = root
        while len(list) > 0 or cur_node is not None:
            if cur_node is not None:
                #middle node
                result.append(cur_node.val)
                list.append(cur_node.right)
                #check left
                cur_node = cur_node.left
            else:
                #right node (stack: FILO)
                cur_node = list.pop(len(list)-1)
        return result

