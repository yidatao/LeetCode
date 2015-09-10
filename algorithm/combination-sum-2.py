class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        self.dfs(candidates, target, [], res, 0, 0)
        return res


    def dfs(self, candidates, target, c, res, start, curSum):
        if curSum == target:
            tmp = list(c)
            #check for duplicates
            if tmp not in res:
                res.append(tmp)
            return

        for i in range(start, len(candidates)):
            #since candidates is already sorted, if their sum is larger than target, no need to go further
            if curSum + candidates[i] > target:
                return
            c.append(candidates[i])
            #since it doesn't allow repetitive elements, start from i+1
            self.dfs(candidates, target, c, res, i+1, curSum + candidates[i])
            c.pop()
