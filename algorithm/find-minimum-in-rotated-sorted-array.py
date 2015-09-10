class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        start, end = 0, len(num)-1
        while start < end:
            mid = (start + end) / 2
            if num[mid] < num[end]:
                end = mid
            else:
                start = mid + 1
        return num[start]

print(Solution().findMin([5,6,7,8,0,1,2,3,4]))