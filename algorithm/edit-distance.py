class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        l1,l2 = len(word1),len(word2)
        dp = [[0 for x in range(l2+1)] for y in range(l1+1)]

        #if word2 is "", delete
        for i in range(l1+1):
            dp[i][0] = i
        #if word1 is "", insert
        for j in range(l2+1):
            dp[0][j] = j

        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if word1[i-1] == word2[j-1]:
                    #no operation is required
                    dp[i][j] = dp[i-1][j-1]
                else:
                    #option 1, delete this char in word1: dp[i-1][j]+1
                    #option 2, insert this char in word1: dp[i][j-1]+1
                    #option 3, replace this char in word1: dp[i-1][j-1]+1
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)

        return dp[l1][l2]