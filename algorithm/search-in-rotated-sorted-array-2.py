class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        start, end = 0, len(A) - 1
        while start <= end:
            mid = (start + end) / 2
            if A[mid] == target:
                return True
            if A[start] < A[mid]:
                if A[start] <= target < A[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif A[start] > A[mid]:
                if A[mid] < target <= A[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            else: #ignore duplicate
                start += 1
        return False

