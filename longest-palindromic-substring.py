class Solution:
    # @return a string
    # This solution's reference: http://www.cnblogs.com/zuoyuan/p/3777721.html
    def longestPalindrome(self, s):
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


print(Solution().longestPalindrome("aaabaaaa"))