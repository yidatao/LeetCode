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


    def combine1(self, n, k):
        return self.func(range(1,n+1), k)

    def func(self, l, k):
        if k == 0: return [[]]
        if l == []: return []
        #don't forget the second part
        return [[l[0]] + x for x in self.func(l[1:], k-1)] + self.func(l[1:], k)

print(Solution().combine1(5,3))