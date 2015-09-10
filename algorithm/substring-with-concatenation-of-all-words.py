class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        res = []

        map = {}
        for s in L:
            if s in map:
                map[s] += 1
            else:
                map[s] = 1

        l = len(L[0])

        left = right = 0
        count = 0
        m = map.copy()
        while right < len(S):
            word = S[right:right+l]
            if word in m and m[word] > 0:
                count += 1
                m[word] -= 1
                if count == len(L):
                    res.append(left)
                    left += 1
                    right = left
                    #reset
                    m = map.copy()
                    count = 0
                else:
                    right += l
            else:
                left += 1
                right = left
                #reset
                m = map.copy()
                count = 0
        return res

print(Solution().findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake",["fooo","barr","wing","ding","wing"]))
