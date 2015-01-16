class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        n = len(s)
        #whether substring si to sj is palindrome
        #this is also assigned via DP
        isPalindrom = [[False for j in range(n)] for i in range(n)]
        #dp[i] is the # of palindromes under the min cut for i to len(s)-1
        #n-i is the maximum possible palindromes by cut on every char
        dp = [n-i for i in range(n+1)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (i==j or i+1==j or isPalindrom[i+1][j-1]):
                    isPalindrom[i][j] = True
                    #i to j is one palindrome, plus # of palindromes in j+1 to n-1
                    dp[i] = min(dp[i], 1 + dp[j+1])

        #don't forget to -1 to get the # of cut
        return dp[0] - 1