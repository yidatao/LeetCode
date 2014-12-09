class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams0(self, strs):
        if len(strs) == 0:
            return []
        signature = {}
        res = []
        strs = sorted(strs, key=lambda l:len(l))
        cur_len = len(strs[0])
        for string in strs:
            if len(string) > cur_len:
                for k,v in signature.items():
                    if len(v) > 1:
                        res += v
                signature = {}
                cur_len = len(string)
            sig = self.get_character(string)
            if sig in signature:
                signature[sig].append(string)
            else:
                signature[sig] = [string]
        #don't forget the last group
        for k,v in signature.items():
            if len(v) > 1:
                res += v
        return res

    #get the string's signature as character:count (sorted by character)
    def get_character(self, string):
        map = {}
        for s in string:
            if s in map:
                map[s] += 1
            else:
                map[s] = 1
        res = ''
        for k in sorted(map):
            res += k + ':' + str(map[k]) + ','
        return res

    def anagrams1(self, strs):
        map = {}
        res = []
        for string in strs:
            #a string's signature is simply its sorted version (no need to count character occurrence)
            sig = ''.join(sorted(string))
            map[sig] = [string] if sig not in map else map[sig] + [string]
        for k,v in map.items():
            if len(v) > 1:
                res += v
        return res

strs = ["",""]
print(Solution().anagrams(strs))