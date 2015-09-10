class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        nums = nums[::-1]
        nums = nums[:k][::-1] + nums[k:][::-1]

print(Solution().rotate([1,2],1))
