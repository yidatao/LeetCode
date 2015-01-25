class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        res, cur_max, cur_min = A[0], A[0], A[0]
        for i in range(1, len(A)):
            x = A[i] * cur_max
            #if A[i] is negative and cur_min is negative, the product may be a large positive
            #so every time we not only remember the current max, but also the current (negative) min
            y = A[i] * cur_min
            cur_max = max(x, y, A[i])
            cur_min = min(x, y, A[i])
            res = cur_max if cur_max > res else res
        return res

print(Solution().maxProduct([2,3,-2,4]))