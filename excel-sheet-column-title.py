class Solution:
    # @return a string
    def convertToTitle(self, num):
        res = '' #reversed
        while num > 0:
            mod = num % 26
            num = num / 26
            if mod == 0:
                res += 'Z'
                num -= 1
            else:
                res += chr(65+mod-1)
        #reverse back
        return res[::-1]


print(Solution().convertToTitle(52))