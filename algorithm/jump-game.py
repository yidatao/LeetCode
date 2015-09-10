class Solution:
    # @param A, a list of integers
    # @return a boolean
    # Time limit exceeded
    def canJump0(self, A):
        #0: can't jump, 1: can jump
        res = [False for x in range(len(A))]
        res[0] = True; i=0
        while i < len(A)-1:
            if not A[i]:
                break
            bound = i+A[i]+1 if i+A[i]+1 < len(A) else len(A)
            if bound == len(A):
                return True
            res[i+1:bound] = [True for x in range(A[i])]
            i += 1
        return res[-1]

    def canJump(self, A):
        #the maximum location that can be reached
        maxLoc = A[0]
        for i in range(len(A)):
            #the if condition suggests: every position before maxLoc can be reached (read the problem carefully)
            if i <= maxLoc:
                #push the maxLoc
                maxLoc = max(maxLoc, i + A[i])
                if maxLoc >= len(A)-1:
                    return True
        return False


print(Solution().canJump([0]))
