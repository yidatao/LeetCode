class Solution:
    # @param A, a list of integers
    # @return an integer
    # time limit exceeded
    def jump0(self, A):
        res = [float("inf") for x in range(len(A))]
        res[0] = 0; i=0
        while i < len(A)-1:
            #cannot reach this step
            if A[i] == float("inf"):
                break
            bound = i+A[i]+1 if i+A[i]+1 < len(A) else len(A)
            for j in range(i+1,bound):
                res[j] = min(res[j],res[i]+1)
            i += 1
        return res[-1]

    #similar concept with jump game I
    ## of minimum steps equals to the steps to reach the maximum distance
    def jump1(self, A):
        if len(A) == 1: return 0
        jump = 0; maxReach = 0
        while True:
            jump += 1
            for i in range(maxReach + 1):
                maxReach = max(maxReach, i+A[i])
                if maxReach >= len(A)-1:
                    return jump


    # suggested online, hard to understand
    #TODO might revisit
    def jump2(self, A):
        minJump = 0
        maxReach = 0
        nextReach = 0 #max reach by minJump+1
        for i in range(len(A)):
            if i > maxReach:
                maxReach = nextReach
                minJump += 1
            nextReach = max(maxReach,i+A[i])
        return minJump

print(Solution().jump1([2,3,1,1,4]))