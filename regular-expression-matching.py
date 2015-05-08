class Solution:
    # @return a boolean
    # Note: this is different from the wildcard problem, since * here should also be considered together with its preceding element
    def isMatch(self, s, p):
        dp = [[False for j in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True
        #if s is "", p matches only if a * is preceded with 1 element or not
        for j in range(1,len(p)+1):
            if p[j-1] == "*":
                if j >= 2:
                    dp[0][j] = dp[0][j-2]

        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    #note j is '*' and j-1 is its preceding
                    #if 0 preceding, then j-2
                    #if 1 preceding, then j-1
                    #if multiple preceding
                    dp[i][j] = dp[i][j-2] or dp[i][j-1] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == "."))
                else:
                    dp[i][j] = dp[i-1][j-1] and s[i-1] == p[j-1]

        return dp[-1][-1]
