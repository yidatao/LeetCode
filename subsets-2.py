class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        res = []
        S.sort()
        self.dfs(S,0,res)
        return res

    def dfs(self, array, i, res):
        if i == len(array):
            res.append([])
        else:
            self.dfs(array, i+1, res)
            #need to copy the res, otherwise its endless since we keep appending to the list
            tmp = list(res)
            for item in tmp:
                l = [array[i]] + item
                if l not in res:
                    res.append(l)

S=[1,2,2]
print(Solution().subsetsWithDup(S))