class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        if n == 0: return 0
        s = []
        while n > 0:
            if n & 1 == 1:
                s = [1] + s
            else:
                s = [0] + s
            n = n >> 1 #shift to right by 1 bit
        
        return sum(s)

    def hammingWeight1(self, n):
        res = 0
        while n > 0:
            res += n % 2
            n >>= 1
        return res