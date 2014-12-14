class Solution:
    # @param height, a list of integer
    # @return an integer
    # O(n^2), time limit exceeded
    def largestRectangleArea(self, height):
        area = 0
        for width in range(1,len(height)+1):
            for i in range(0, len(height)-width+1):
                a = width * min(height[i:(i+width)])
                if a > area:
                    area = a
        return area

    #still time limit exceeded
    def largestRectangleArea1(self, height):
        area = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                a = (j-i+1)*min(height[i:j+1])
                if a > area:
                    area = a
                elif a < area:
                    break
        return area

    #TODO need to revisit this
    def largestRectangleArea2(self, height):
        stack = [] #keep non-decreasing indice
        maxArea = 0
        i = 0
        height.append(0) #dummy height to consider all heights
        while i < len(height):
            if len(stack) == 0 or height[stack[-1]] <= height[i]:
                stack.append(i)
                i += 1
            else:
                t = stack.pop()
                width = i if len(stack)==0 else i-stack[-1]-1
                maxArea = max(maxArea, height[t]*width)
        return maxArea


print(Solution().largestRectangleArea2([2,1,5,6,2,3]))