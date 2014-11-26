class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        solution = []
        self.search(root,sum,0,[],solution)
        return solution

    def search(self, root, sum, cur_sum, cur_list, solution):
        if root is None:
            return
        cur_sum = root.val + cur_sum
        #leaf
        if root.left is None and root.right is None:
            if cur_sum == sum:
                solution.append(cur_list+[root.val])
        if root.left:
            self.search(root.left, sum, cur_sum, cur_list+[root.val], solution)
        if root.right:
            self.search(root.right, sum, cur_sum, cur_list+[root.val], solution)


