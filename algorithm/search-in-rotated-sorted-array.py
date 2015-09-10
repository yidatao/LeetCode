class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        l, r = 0, len(A) - 1
        while l <= r:
            mid = (l+r) / 2
            if A[mid] == target:
                return mid
            #left part is increasing
            if A[mid] >= A[l]:
                #search left
                if A[l] <= target < A[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else: #right part is increasing
                #search right
                if A[mid] < target <= A[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
