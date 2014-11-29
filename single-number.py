class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        A.sort()
        i = 0
        while i < len(A)-1 and A[i] == A[i+1]:
            i += 2
        return A[i]

    #use xor
    def singleNumber1(self, A):
        res = A[0]
        for i in range(1,len(A)):
            res = res ^ A[i]
        return res

print(Solution().singleNumber([1,2,1,3,3,2,0,0,4,5,4]))