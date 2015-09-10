class Solution:
    # @param A, a list of integers
    # @return an integer
    # DP solution
    def maxSubArray(self, A):
        dp = [0 for x in range(len(A))]
        dp[0] = A[0]
        for i in range(1, len(A)):
            dp[i] = max(dp[i-1] + A[i], A[i])
        return max(dp)

    #divide and conquer
    def maxSubArray1(self, A):
        return self.findMax(A, 0, len(A)-1)

    def findMax(self, A, left, right):
        #don't forget the return condition
        if left == right: return A[left]
        mid = (left + right) / 2
        #if A[mid] is not in the resulting subarray
        #case 1: result in left, mid - 1
        leftMax = self.findMax(A, left, mid)
        #case 2: result in mid + 1, right
        rightMax = self.findMax(A, mid + 1, right)
        #case 3: if A[mid] in the resulting subarray
        #find i~mid with max sum and mid+1~j with max sum and add them
        lMax = A[mid]
        lSum = A[mid]
        for i in range(mid-1, left-1, -1):
            lSum += A[i]
            lMax = max(lMax, lSum)
        rMax = A[mid+1]
        rSum = A[mid+1]
        for i in range(mid+2, right+1):
            rSum += A[i]
            rMax = max(rMax, rSum)
        return max(leftMax, rightMax, lMax + rMax)

print(Solution().maxSubArray1([-2,1,-3,4,-1,2,1,-5,4]))
