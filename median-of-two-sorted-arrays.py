class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        m,n = len(A),len(B)
        if (m+n) % 2 == 1:
            return self.getKthSmallest(A, B, (m+n+1)/2)
        else:
            return 0.5 * (self.getKthSmallest(A,B,(m+n)/2) + self.getKthSmallest(A,B,(m+n)/2+1))

    #reference: http://chaoren.is-programmer.com/posts/42890.html
    #reference: http://www.cnblogs.com/zuoyuan/p/3759682.html
    def getKthSmallest(self, A, B, k):
        #assume len(A) <= len(B)
        if len(A) > len(B):
            return self.getKthSmallest(B, A, k)
        #so A should be the first to reduce to []
        if len(A) == 0:
            return B[k-1]
        if k == 1:
            return min(A[0],B[0])
        #althought the reference uses k/2 as an example, the length of A might become smaller than k/2
        ia = min(k/2, len(A))
        #ib + ia == k
        ib = k - ia
        return self.getKthSmallest(A[ia:],B,ib) if A[ia-1] < B[ib-1] else self.getKthSmallest(A,B[ib:],ia)