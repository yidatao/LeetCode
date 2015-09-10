class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    # referred to http://bookshadow.com/weblog/2015/04/17/leetcode-bitwise-and-numbers-range/
    def rangeBitwiseAnd(self, m, n):
        shift = 0
        #find the common left header (or, prefix) of m and n
        while m != n:
            m >>= 1 #shift to right by 1 bit
            n >>= 1
            shift += 1
        #then shift to left (the remaining bits are not the same, so definitely result in 0 after AND)
        return m << shift