class Solution:
    # @return a list of integers
    def grayCode(self, n):
        size = 1 << n
        res = []
        for i in range(size):
            t = i >> 1
            res.append(i ^ t)
        return res

print(Solution().grayCode(2))