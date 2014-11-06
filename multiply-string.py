class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        return str(int(num1)*int(num2))

if __name__ == '__main__':
    print(Solution().multiply('123','456'))