class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    # Time limit exceeded
    def combinationSum0(self, candidates, target):
        subsets = []
        candidates.sort()
        self.dfs(candidates,0,subsets)

        map = {}
        for ss in subsets:
            s = sum(ss)
            if s > 0 and s <= target:
                if s in map:
                    map[s].append(ss)
                else:
                    map[s] = [ss]

        res = []
        for k,v in map.items():
            if k == target:
                for vv in v:
                    res.append(sorted(vv))
            else:
                if target - k in map:
                    for vv in v:
                        for value in map[target-k]:
                            r = sorted(vv + value)
                            if r not in res:
                                res.append(r)

        return res

    def dfs0(self, array, i, subsets):
        #reach the leaf
        if i == len(array):
            subsets.append([])
        else:
            #first process its deeper (by 1) layer
            self.dfs(array, i+1, subsets)
            #then append the current element to all the subsets of the deeper layer
            subsets.extend([[array[i]] + item for item in subsets])


    def combinationSum(self, candidates, target):
        candidates.sort()
        res = []
        self.dfs(candidates, target, [], res, 0, 0)
        return res


    def dfs(self, candidates, target, c, res, start, curSum):
        if curSum == target:
            res.append(list(c))
            return

        for i in range(start, len(candidates)):
            #since candidates is already sorted, if their sum is larger than target, no need to go further
            if curSum + candidates[i] > target:
                return
            c.append(candidates[i])
            #since it allows repetitive elements, start is index i instead of i+1
            self.dfs(candidates, target, c, res, i, curSum + candidates[i])
            c.pop()

print(Solution().combinationSum([2,3,6,7,11,12],14))