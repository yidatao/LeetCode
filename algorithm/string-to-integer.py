class Solution:
    # @return an integer
    def atoi(self, string):
        INT_MAX = 2147483647; INT_MIN = -2147483648; bound = INT_MAX/10
        string = string.strip()
        sign = 1
        if string.startswith('+'):
            string = string[1:]
        elif string.startswith('-'):
            sign = -1
            string = string[1:]

        res = 0
        i = 0
        while i<len(string) and string[i].isdigit():
            num = int(string[i])
            if(res>bound or (res==bound and num > 7)):
                return INT_MAX if sign == 1 else INT_MIN
            res = res * 10 + num #this is the key computation for processing int from left to right, digit by digit
            i += 1
        return res*sign

print(Solution().atoi("2147483648"))