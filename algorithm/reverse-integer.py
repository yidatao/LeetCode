class Solution:
    # @return an integer
    def reverse(self, x):
        #consider negative integers
        negative = True if x < 0 else False
        x=abs(x)
        res = int(str(x)[::-1])
        return -res if negative else res

if __name__ == '__main__':
    print(Solution().reverse(12345))