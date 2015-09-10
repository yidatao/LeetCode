class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        #first sort the list
        num.sort()
        return self.permute(num)

    def permute(self, num):
        if len(num) <= 1:
            return [num]
        res = []
        prev = None
        for i in range(len(num)):
            if num[i] == prev: continue
            prev = num[i]
            for p in self.permute(num[:i] + num[i+1:]):
                res.append([num[i]] + p)
        return res