class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        #don't forget the boundary condition
        if x == 0:
            return 0
        if n == 0:
            return 1

        #recursion
        return x * pow(x,n-1)

if __name__ == '__main__':
    print(Solution().pow(2,10))