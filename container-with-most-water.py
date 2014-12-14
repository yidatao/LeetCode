class Solution:
    # @return an integer
    # O(n^2)
    def maxArea0(self, height):
        area = 0
        for i in range(len(height)-1):
            for j in range(i+1,len(height)):
                h = height[j] if height[j] < height[i] else height[i]
                a = abs(i-j) * h
                if a > area:
                    area = a
        return area

    #complexity O(n)
    def maxArea(self, height):
        left, right = 0, len(height)-1
        area = 0
        while left < right:
            a = (right - left) * min(height[left],height[right])
            if a > area:
                area = a
            #decide how to move the index. Since width must decrease, we should look for larger height
            #In other words, we want to keep the already larger height, and move index of the smaller height index in order to find a larger one
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area


print(Solution().maxArea([1,1]))