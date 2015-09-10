class Solution:
    # @param s, a string
    # @return a string
    def reverseWords0(self, s):
        #reverse the entire string first, then reverse each word
        words = s[::-1].split() #in python, split() by default takes care of whitespace(s)
        res = []
        for word in words:
            res.append(word[::-1])
        return ' '.join(res)

    def reverseWords1(self, s):
        #split, then merge the words reversely
        words = s.split()[::-1]
        return ' '.join(words)

