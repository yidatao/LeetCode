class Solution:
    # @param an integer
    # @return a list of string
    # recursion while return a list
    def generateParenthesis(self, n):
        if n == 0:
            return []
        res = []
        self.func(n,n,'',res)
        return res

    #left, right are the remaining number of l/r parenthesis that can be used
    def func(self, left, right, item, res):
        #this indicates we used more ) than ( so far, which is unacceptable
        if right < left:
            return
        if left == right == 0:
            res.append(item)
        if left > 0:
            self.func(left-1,right,item+'(',res)
        if right > 0:
            self.func(left,right-1,item+')',res)

print(Solution().generateParenthesis(3))