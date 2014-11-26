class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) < 2:
            return len(A)
        #two pointers
        i = 1
        j = 0
        while i < len(A):
            #only two cases: equal or not equal
            if A[i] == A[j]:
                #if equal/duplicate, ignore and go on
                i += 1
            else:
                #if not, remember the next distinct element
                j += 1
                A[j] = A[i]
                i += 1
        A = A[:j+1]
        return len(A)