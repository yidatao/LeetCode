class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    # TLE if directly use DFS
    def wordBreak(self, s, dict):
        res = []
        self.dfs(s, dict, "", res)
        return res

    def dfs(self, s, dict, sentence, res):
        if self.check(s, dict):
            if len(s) == 0:
                #remove the last space
                res.append(sentence[:-1])
            for i in range(1, len(s)+1):
                if s[:i] in dict:
                    self.dfs(s[i:], dict, sentence + s[:i] + ' ', res)


    def check(self, s, dict):
        #dp[i] means whether s[:i-1] can be segmented
        dp = [False for x in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for k in range(i):
                if dp[k] and s[k:i] in dict:
                    dp[i] = True
        return dp[-1]

print(Solution().wordBreak("catsanddog",["cat", "cats", "and", "sand", "dog"]))