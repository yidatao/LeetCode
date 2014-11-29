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


print(Solution().singleNumber1([1,2,1,3,3]))