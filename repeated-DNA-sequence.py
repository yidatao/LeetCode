class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        smap = {}
        for i in range(len(s)-9):
            ss = s[i:i+10]
            sint = self.toInt(ss)
            smap[sint] = 1 if sint not in smap else smap[sint]+1
        res = []
        decode = {0:'A',1:'C',2:'G',3:'T'}
        for k,v in smap.items():
            if v > 1:
                s = ""
                for i in range(10):
                    s = decode[k&3] + s
                    k >>= 2
                res += [s]
        return res
    
    def toInt(self, s):
        res = 0
        code = {'A':0,'C':1,'G':2,'T':3}
        for c in s:
            res += code[c]
            res <<= 2
        return res >> 2


print(Solution().findRepeatedDnaSequences("GAGAGAGAGAGA"))