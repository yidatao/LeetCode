class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations0(self, digits):
        if digits == "": return [""]
        self.letters = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        res = []
        self.combine(digits, res)
        #since res now also contains temporary results produced in recursion, remove them
        res = [x for x in res if len(x)==len(digits)]
        return res

    def combine(self, digits, res):
        if len(digits) == 1:
            for c in self.letters[int(digits[0])]:
                res.append(c)
            return

        letter = self.letters[int(digits[0])]
        self.combine(digits[1:], res)
        tmp = list(res)
        for c in letter:
            for r in tmp:
                res.append(c+r)

    def letterCombinations(self, digits):
        self.letters = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        res = []
        self.length = len(digits)
        self.dfs(0, '', res, digits)
        return res

    def dfs(self, index, curStr, res, digits):
        if index == self.length:
            res.append(curStr)
            return
        for c in self.letters[int(digits[index])]:
            self.dfs(index+1, curStr + c, res, digits)

