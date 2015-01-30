class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        #dp[i] means whether s[:i-1] can be segmented
        dp = [False for x in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for k in range(i):
                if dp[k] and s[k:i] in dict:
                    dp[i] = True
        return dp[-1]

print(Solution().wordBreak("leetcode",['leet','code']))