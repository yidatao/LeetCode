class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    # TODO need to revisit this problem
    def subsets(self, S):
        res = []
        S.sort()
        self.dfs(S,0,res)
        return res

    def dfs(self, array, i, res):
        #reach the leaf
        if i == len(array):
            res.append([])
        else:
            #first process its deeper (by 1) layer
            self.dfs(array, i+1, res)
            #then append the current element to all the subsets of the deeper layer
            res.extend([[array[i]] + item for item in res])

S=[1,2,2]
print(Solution().subsets(S))