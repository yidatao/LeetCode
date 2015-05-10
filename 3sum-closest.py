class Solution:
    # @return an integer
    def threeSumClosest(self, nums, target):
        distance = float("inf")
        res = None
        nums.sort()
        for i in range(len(nums)-2):
            a = nums[i]
            j,k = i+1, len(nums)-1
            while j < k:
                b,c = nums[j], nums[k]
                s = a + b + c
                if s == target:
                    return s
                elif s > target:
                    if s - target < distance:
                        distance = s - target
                        res = s
                    k -= 1
                else:
                    if target - s < distance:
                        distance = target - s
                        res = s
                    j += 1
        return res

print(Solution().threeSumClosest([-1,2,1,-4],1))