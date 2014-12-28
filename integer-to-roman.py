class Solution:
    # @return a string
    def intToRoman(self, num):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = ''
        for i in range(len(val)):
            while num >= val[i]:
                res += roman[i]
                num -= val[i]
        return res

print(Solution().intToRoman(10))
