class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        if len(A)==0:
            return [-1,-1]
        start, end = 0, len(A) -1
        while start + 1 < end:
            mid = (start + end) / 2
            if A[mid] == target:
                end = mid #push to left to find the leftmost index
            elif A[mid] < target:
                start = mid
            else:
                end = mid
        #left bound
        if A[start] == target:
            left = start
        elif A[end] == target:
            left = end
        else:
            return [-1,-1]

        start, end = 0, len(A) -1
        while start + 1 < end:
            mid = (start + end) / 2
            if A[mid] == target:
                start = mid #push to right to find the rightmost index
            elif A[mid] > target:
                end = mid
            else:
                start = mid

        if A[end] == target:
            right = end
        elif A[start] == target:
            right = start
        else:
            return [-1,-1]

        return [left,right]
