class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num = sorted([str(x) for x in num], cmp = self.compare)
        #strip the leading zeros
        res = ''.join(num).lstrip('0')
        #if res = '', then return '0'
        return res or '0'

    #customized comparison for x+y and y+x
    def compare(self, x, y):
        if x == y: return 0
        return 1 if x+y < y+x else -1