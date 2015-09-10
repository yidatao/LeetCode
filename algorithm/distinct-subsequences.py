class Solution:
    # @return an integer
    # DP
    # TODO need to revisit
    def numDistinct(self, S, T):
        l1, l2 = len(S), len(T)
        #note dp[0][0] = 1, meaning S and T are both empty, so there is only 1 distinct subsequence
        #dp[i][0] = 1, meaning T is "", only 1 distinct subsequence since all chars in s need to be deleted
        dp = [[1 for x in range(l2+1)] for y in range(l1+1)]
        for i in range(1, l2+1):
            #if S is ""
            dp[0][i] = 0
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if S[i-1] == T[j-1]:
                    #two options
                    #1st, match this char, check the previous dp[i-1][j-1]
                    #2nd, don't match this char (delete this char), then check dp[i-1][j]
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[l1][l2]
