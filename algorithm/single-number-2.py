class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber0(self, A):
        A.sort()
        i = 0
        while i < len(A)-2 and A[i] == A[i+1] and A[i] == A[i+2]:
            i += 3
        return A[i]

    #TODO bit-vector solution?
    #Reference: http://jelices.blogspot.hk/2014/06/leetcode-python-single-number-ii.html
    def singleNumber1(self, nums):
        one,two,three = 0,0,~0
        for x in nums:
            one1 = (three & x) | (one & ~x)
            two1 = (one & x) | (two & ~x)
            three1 = (two & x) | (three & ~x)
            one,two,three = one1,two1,three1
        return one

print(Solution().singleNumber1([1,2,1,3,3]))