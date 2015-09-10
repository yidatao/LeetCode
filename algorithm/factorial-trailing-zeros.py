class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        res = 0
        x = 5
        while n > x:
            res += n / x
            x *= 5
        return res