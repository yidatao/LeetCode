class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        start, end = 0, len(num)-1
        while start < end:
            mid = (start + end) / 2
            if num[mid] < num[end]:
                end = mid
            elif num[mid] > num[end]:
                start = mid + 1
            else:
                end -= 1
        return num[start]