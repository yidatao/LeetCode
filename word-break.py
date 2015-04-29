class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        #dp[i] means whether s[:i] can be segmented
        dp = [False for x in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for k in range(i):
                if dp[k] and s[k:i] in dict:
                    dp[i] = True
        return dp[-1]

    #TLE
    def wordBreak1(self, s, wordDict):
        if wordDict is None or len(wordDict) == 0: return False
        if s == "": return True
        for word in wordDict:
            if s.startswith(word) and self.wordBreak(s[len(word):], wordDict):
                    return True
        return False

print(Solution().wordBreak1("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))