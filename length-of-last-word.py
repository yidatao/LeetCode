class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        tmp = s.strip().split()
        return len(tmp[-1]) if len(tmp) > 0 else 0

print(Solution().lengthOfLastWord(""))