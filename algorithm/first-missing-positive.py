class Solution:
    # @param A, a list of integers
    # @return an integer
    # Since only constant space is required, we can simply compute in place (using the given array itself)
    # The array's indices can be used naturally as consecutive integers
    # Place any value x to A[x-1], e.g., A[2] = 3, given the index exists
    def firstMissingPositive(self, A):
        i = 0
        while i < len(A):
            x = A[i]
            #first need to ensure x-1 is a valid index
            #then, if x-1 already equals to the index i, then it's already in place, no need to swap, just move on (otherwise it goes on and on)
            #then if x equals to A[x-1], which is the value being swapped, then also no need to swap, just move on to the else branch
            if x >= 1 and x <= len(A) and x-1 != i and x != A[x-1]:
                #python's swap
                #the swap happens because we need to process every number in A
                #so don't increase i after swap: need to process the swapped/new number
                A[x-1], A[i] = x, A[x-1]
            else:
                i += 1

        for i in range(len(A)):
            #judge. A should now be [1,2,3,4,5,...]. The first violation indicates the first missing positive value
            if A[i] != i+1:
                return i+1

        #don't forget this! even though the array is [1,2,3], need to return 4 as the first missing positive value
        return len(A)+1

print(Solution().firstMissingPositive([1,1]))