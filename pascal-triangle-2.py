class Solution:
    # @return a list of integers
    # TODO: O(k) space?
    def getRow(self, rowIndex):
        res = [[1]]
        for i in range(1, rowIndex+1):
            l = [1 for x in range(i+1)]
            for j in range(1,i):
                l[j] = res[i-1][j-1] + res[i-1][j]
            res.append(l)
        return res[-1]

print(Solution().getRow(3))