class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        map = {}
        for i in num:
            if i in map:
                map[i] += 1
            else:
                map[i] = 0
        return sorted(map.items(), key=lambda k:k[1])[-1][0]

print(Solution().majorityElement([2,2,2,3]))