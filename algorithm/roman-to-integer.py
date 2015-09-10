class Solution:
    # @return an integer
    def romanToInt(self, s):
        trans = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        res = 0
        #reverse the string
        s = s[::-1]
        #record the current highest value
        high = 0
        for c in s:
            #in this case, minus; else, simply add the value and reset the high
            if trans[c] < high:
                res -= trans[c]
            else:
                res += trans[c]
                high = trans[c]
        return res

print(Solution().romanToInt("M"))