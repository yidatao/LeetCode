class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        res = []
        self.dfs(1, n, k, [], res)
        return res

    def dfs(self, start, n, k, c, res):
        if len(c) == k:
            #copy it, since we need to operate on this list later
            tmp = list(c)
            res.append(tmp)
            return

        for i in range(start, n+1):
            c.append(i)
            self.dfs(i+1, n, k, c, res)
            #remove this element and try another
            c.pop()

print(Solution().combine(5,3))