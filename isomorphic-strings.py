class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        smap = {}
        tmap = {}
        for i in range(len(s)):
            if s[i] not in smap:
                if t[i] in tmap and s[i] != t[i]: return False
                smap[s[i]] = t[i]
                tmap[t[i]] = s[i]
            elif t[i] != smap[s[i]]:
                    return False
        return True