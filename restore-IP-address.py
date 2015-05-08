class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        if not s.isdigit(): return []
        self.res = []
        self.func(0, '', s)
        return self.res

    def func(self, part, val, remainStr):
        if part == 3:
            #str(int(s)) == s ensures s doesn't start with 0 (int(s) automatically removes starting 0s)
            if str(int(remainStr)) == remainStr and int(remainStr) <= 255:
                #val[1:] to remove the very first '.'
                self.res.append(val[1:]+'.'+remainStr)
            return
        #each ip part can have 1,2,or 3 digits
        #traverse each possibility, and recursively call func on the remaining substring
        for i in range(1,4):
            if i >= len(remainStr):
                break
            curPart = remainStr[:i]
            if str(int(curPart)) == curPart and int(curPart) <= 255:
                self.func(part+1, val+'.'+curPart, remainStr[i:])

    def restoreIpAddresses1(self, s):
        res = []
        self.recur(s, 4, "", res)
        return res

    def recur(self, s, part, curr, res):
        if part == 1:
            if s!= "" and str(int(s)) == s and int(s) <= 255:
                curr += "." + s
                res.append(curr[1:])
            return
        for i in range(3):
            if i >= len(s): return
            p = s[:i+1]
            if str(int(p))==p and int(p) <= 255:
                self.recur(s[i+1:], part-1, curr + "." + p, res)