class Solution:
    # @param s, a string
    # @return a list of lists of string
    # This type of solution can be generalized to many different problems
    def partition(self, s):
        res = []
        self.func(s, [], res)
        return res

    def func(self, s, curlist, res):
        if len(s) == 0:
            res.append(list(curlist))
            return
        for i in range(len(s)):
            if s[:i+1] == s[:i+1][::-1]:
                curlist.append(s[:i+1])
                self.func(s[i+1:], curlist, res)
                curlist.pop()

print(Solution().partition("aab"))
