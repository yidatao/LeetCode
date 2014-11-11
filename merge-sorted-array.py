class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge0(self, A, m, B, n):
        if len(A)==0 or len(B)==0:
            A.extend(B)
            return
        i = 0
        j = 0
        while j < n:
            a = A[i]
            b = B[j]
            if b > a:
                i += 1
                if i >= len(A):
                    A.extend(B[j:])
                    break
            else:
                A.insert(i, b)
                i += 1
                j += 1

    def merge1(self, A, m, B, n):
        i,j,k = m-1,n-1,m+n-1
        #insert from the back
        while i>=0 and j>=0:
            if A[i] >= B[j]:
                A[k] = A[i]
                i -= 1
            else:
                A[k] = B[j]
                j -= 1
            k -= 1

        #in case B is left
        while j>=0:
            A[k] = B[j]
            k -= 1
            j -= 1


A = [1,3,4,0,0]
B = [1,2]
Solution().merge1(A,3,B,2)
print(A)
