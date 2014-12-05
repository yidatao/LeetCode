class Solution:
    # @param n, an integer
    # @return an integer
    # Dynamic programming
    def climbStairs(self, n):
        if n<=2:
            return n
        array = [1 for x in range(n)]
        array[1] = 2
        for i in range(2,n):
            array[i] = array[i-2] + array[i-1]
        return array[n-1]

print(Solution().climbStairs(3))