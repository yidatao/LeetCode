class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        start, end = 0, len(A)-1
        while start <= end:
            mid = (start + end) / 2
            if A[mid] == target:
                return mid
            elif A[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return start

    def searchInsert1(self, nums, target):
        for i in range(len(nums)):
            if i == 0 and target < nums[i]: return 0
            if target == nums[i]: return i
            if i < len(nums) - 1 and target > nums[i] and target < nums[i+1]: return i+1
            i += 1
        return len(nums)

print(Solution().searchInsert1([1],0))