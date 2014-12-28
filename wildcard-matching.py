class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        #pointer to explore s and p
        sp = pp = 0
        #the last matched location in s
        smatch = -1
        #the location of a previous * in p
        star = -1
        while sp < len(s):
            #match, go on
            if pp < len(p) and (s[sp] == p[pp] or p[pp] == '?'):
                sp += 1
                pp += 1
                continue
            #if p has a *, of course we can use it to match ""
            #but still we need to save it in case there is mismatch later
            elif pp < len(p) and p[pp] == '*':
                star = pp
                #here only pp moves on, sp stays, meaning for now we assume * matches empty string
                pp += 1
                smatch = sp
                continue
            #a mismatch happens
            elif star != -1:
                #use * to match the unmatched element in s
                pp = star + 1
                smatch += 1
                sp = smatch
                continue
            else:
                return False

        #check the remaining p (only if pp already reach the end or the remaining p is all '*', then it's a match)
        if pp == len(p):
            return True
        if p[pp:] == '*'*(len(p)-pp):
            return True
        return False


