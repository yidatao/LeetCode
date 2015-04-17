class Solution:
    # @return a string
    # This solution's reference: http://www.cnblogs.com/zuoyuan/p/3777721.html
    def longestPalindrome0(self, s):
        res = ""
        for i in range(len(s)):
            #odd
            p1 = self.getLongestPalindrome(s, i, i)
            if len(p1) > len(res):
                res = p1
            #even
            p2 = self.getLongestPalindrome(s, i, i+1)
            if len(p2) > len(res):
                res = p2
        return res


    #pivot is (index, index) or (index, index+1)
    #push to left and right simultaneously
    def getLongestPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    #TLE
    def longestPalindrome(self, s):
        dp = [[0 for y in range(len(s)+1)] for x in range(len(s)+1)]
        dp[0][0] = 0
        maxLength = 0
        for i in range(len(s),0,-1):
            for j in range(i, len(s) + 1):
                if i == j:
                    dp[i][j] = 1
                elif s[i-1] == s[j-1]:
                    if i+1 == j:
                        dp[i][j] = 2
                    elif i+2 == j:
                        dp[i][j] = 3
                    elif dp[i+1][j-1]:
                        dp[i][j] = dp[i+1][j-1] + 2
                if dp[i][j] > maxLength:
                    maxLength = dp[i][j]
                    indices = (i,j)

        return s[indices[0]-1:indices[1]]



print(Solution().longestPalindrome("aaaabaaaa"))