import re
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        #use regular expression to strip non-alphanumeric characters
        s1 = (re.sub(r'\W+', '', s)).lower()
        return s1 == s1[::-1]

print(Solution().isPalindrome('A man, a plan, a canal: Panama'))
print(Solution().isPalindrome('race a car'))