class Solution:
    # @return an integer
    # Dynamic programming
    def numTrees(self, n):
        #cause we also consider the base case 0
        res = [0 for x in range(n+1)]
        res[0],res[1] = 1,1
        #fill in the dp array
        for i in range(2,n+1):
            #i is the given number of nodes
            #j: all possible number of nodes for the left tree of i
            #so i-j-1 is the number of nodes for the right tree of i (1 is the root)
            for j in range(i):
                #the number of unique trees for i = num of unique left trees * num of unique right trees
                res[i] += res[j] * res[i-j-1]
        return res[n]
