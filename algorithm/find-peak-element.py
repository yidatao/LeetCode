class Solution:
    # @param num, a list of integer
    # @return an integer
    # complexity O(n)
    def findPeakElement0(self, num):
        if len(num) == 1:
            return 0
        for i in range(1,len(num)-1):
            if num[i-1] < num[i] and num[i] > num[i+1]:
                return i
        if num[0] > num[1]:
            return 0
        if num[-1] > num[-2]:
            return len(num)-1

    #complexity O(logn) (binary search)
    def findPeakElement1(self, num):
        start, end = 0, len(num)-1
        #if start + 1 = end, then there is no mid
        while start + 1 < end:
            mid = (start + end) // 2
            if num[mid-1] < num[mid] and num[mid] > num[mid+1]:
                return mid
            elif num[mid-1] > num[mid]:
                end = mid - 1
            elif num[mid] < num[mid+1]:
                start = mid+1
        return start if num[start] > num[end] else end

print(Solution().findPeakElement1([0,1]))