class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        sp, pp = 0, 0
        smatch, star = -1, -1
        while sp < len(s):
            if pp < len(p) and ( p[pp] == '?' or p[pp] == s[sp]):
                pp += 1
                sp += 1
                continue
            elif pp < len(p) and p[pp] == '*':
                star = pp
                pp += 1
                smatch = sp
                continue
            elif pp < len(p) and p[pp] != s[sp]:
                pp = star + 1
                smatch += 1
                sp = smatch
            else:
                return False

        if pp == len(p) or p[pp:] == '*'*(len(p) - pp):
            return True
        return False
