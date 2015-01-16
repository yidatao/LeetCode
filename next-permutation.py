class Solution:
    # @param num, a list of integer
    # @return a list of integer
    # This algorithm is from http://fisherlei.blogspot.hk/2012/12/leetcode-next-permutation.html
    def nextPermutation(self, num):
        loc = -1
        #from right to left, find the first location that violates the increasing order
        for i in range(len(num)-1, 0, -1):
            if num[i-1] < num[i]:
                loc = i-1
                break
        #if such a location is not found, then it means it reaches the end permutation
        #return the first permutation by simply reversing it
        if loc == -1:
            return num[::-1]
        #from right to left, find the first element that is greater than num[loc], swap them
        for i in range(len(num)-1, loc, -1):
            if num[i] > num[loc]:
                num[i], num[loc] = num[loc], num[i]
                break
        #now all elements to the right of loc are in descending order (or in ascending order from right to left)
        #revese them
        return num[:loc+1] + num[loc+1:][::-1]