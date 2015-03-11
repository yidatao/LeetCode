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

    #Use extra m+n space
    def findMedianSortedArrays0(self, A, B):
        pa, pb = 0, 0
        m, n = len(A), len(B)
        C = []
        while pa < m and pb < n:
            if A[pa] <= B[pb]:
                C.append(A[pa])
                pa += 1
                continue
            else:
                C.append(B[pb])
                pb += 1
                continue
        if pa < m:
            C += A[pa:]
        if pb < n:
            C += B[pb:]
        if (m+n) % 2 == 1:
            return C[(m+n)/2]
        else:
            return 0.5 * (C[(m+n)/2]+C[(m+n)/2-1])