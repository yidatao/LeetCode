class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        water = 0
        leftHighest = 0
        #i's left highest bar
        leftHigh = [0 for x in range(len(A))]
        #since the first element has no left bar (or 0), just start from the second element
        for i in range(1,len(A)):
            if A[i-1] > A[i]:
                leftHighest = max(leftHighest, A[i-1])
            leftHigh[i] = leftHighest
        #again, the first and last location cannot contain water anyway
        rightHighest = 0
        for j in range(len(A)-2,0,-1):
            if A[j+1] > A[j]:
                rightHighest = max(rightHighest, A[j+1])
            #only if i has higher bar both on left and right can it trap water
            if min(leftHigh[j], rightHighest) > A[j]:
                water += min(leftHigh[j], rightHighest) - A[j]
        return water

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
