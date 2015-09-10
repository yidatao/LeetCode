class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if len(A) <= 1:
            return A
        i = 0
        j = len(A)-1
        k = 0
        while i<=j:
            if A[i] == 0:
                if i == k:
                    i += 1
                    k += 1
                else:
                    tmp = A[k]
                    A[k] = A[i]
                    A[i] = tmp
                    k += 1
            elif A[i] == 1:
                i += 1
            elif A[i] == 2:
                while A[j] == 2 and i<j:
                    j -= 1
                if i == j:
                    break
                tmp = A[j]
                A[j] = A[i]
                A[i] = tmp
        return A

    #simple version, but same method
    def sortColors1(self, A):
        if len(A) == 0:
            return A
        i = 0 #process elements one by one
        j = len(A)-1 #pointer to the 2's position, from the back
        k = 0 #pointer to the 0's position, from the start
        while i <= j:
            if A[i] == 0: #move to front
                A[i],A[k] = A[k],A[i] #pythonic way to swap elements
                k += 1
                i += 1 #move i since A[i] is already processed
            elif A[i] == 1:
                i += 1
            elif A[i] == 2: #move to back
                A[i],A[j] = A[j],A[i]
                j -= 1 #here don't move i, since A[i] now is not yet processed
        return A
