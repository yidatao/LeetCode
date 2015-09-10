class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i = 1 #pointer for exploration
        j = 0 #pointer to the in-place "results"
        count = 1
        while i < len(A):
            #3 possibilities
            if A[i] == A[j]:
                if count == 2:
                    i += 1
                    continue
                else:
                    count += 1
            else:
                count = 1 #reset since new distinct element is met
            j += 1
            A[j] = A[i]
            i += 1
        A = A[:j+1]
        return len(A)

print(Solution().removeDuplicates([1,1,1]))