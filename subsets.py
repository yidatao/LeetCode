class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    # TODO need to revisit this problem
    def subsets1(self, S):
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

    def subsets(self, S):
        res = []
        S.sort()
        self.recur(S, res)
        return res

    def recur(self, S, res):
        if len(S) == 0:
            res.append([]);
        else:
            self.recur(S[:-1], res)
            tmp = list(res)
            for ss in tmp:
                res.append(ss + [S[-1]])

    #Bit manipulation
    def subsets2(self, S):
        S.sort()
        l = len(S)
        ssize = 2 ** l #size of all subsets
        res = []
        for i in range(ssize):
            tmp = []
            for j in range(l):
                if (i >> j) & 1:
                    tmp.append(S[j])
            res.append(tmp)
        return res


S=[1,2,3]
print(Solution().subsets(S))