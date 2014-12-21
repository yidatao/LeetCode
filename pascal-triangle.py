class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            l = [1 for x in range(i+1)]
            for j in range(1,i):
                l[j] = res[i-1][j-1] + res[i-1][j]
            res.append(l)
        return res

print(Solution().generate(5))
