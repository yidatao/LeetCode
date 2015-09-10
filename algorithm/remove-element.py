class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if len(A) == 0:
            return 0
        i=0
        j=len(A)-1
        while i <= j:
            if A[i] == elem:
                if A[j] == elem:
                    j -= 1
                else:
                    temp = A[i]
                    A[i] = A[j]
                    A[j] = temp
                    i += 1
                    j -= 1
            else:
                i += 1
        return j+1

print(Solution().removeElement([2,3,3,2,1,1,3],3))