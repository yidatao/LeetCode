class Solution:
    # @return a boolean
    def isPalindrome0(self, x):
        if x < 0:
            return False
        num = str(x)
        return num == num[::-1]

    def isPalindrome1(self, x):
        if x < 0:
            return False
        num = str(x)
        if len(num) == 1:
            return True
        if len(num) == 2:
            return True if num[0] == num[1] else False
        #recusion
        return (num[0] == num[len(num)-1]) and self.isPalindrome1(int(num[1:len(num)-1]))

    def isPalindrome2(self, x):
        if x < 0:
            return False
        origin = x
        reverse = 0
        while x > 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x = x // 10 #Python 3, true division (instead of the classic division in Python 2.x)
        return origin == reverse

if __name__ == '__main__':
    print(Solution().isPalindrome1(12321))