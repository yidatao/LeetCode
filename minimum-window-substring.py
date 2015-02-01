class Solution:
    # @return a string
    def minWindow(self, S, T):
        res = ""
        if S is None or T is None or len(S) == 0 or len(T) == 0: return res

        map = {}
        for s in T:
            if s in map:
                map[s] += 1
            else:
                map[s] = 1

        left = right = count = 0
        windowLen = len(S) + 1
        while right < len(S):
            if S[right] in T:
                map[S[right]] -= 1
                #if < 0, meaning that S contains more S[right] than T does, used later to know when can push the left boundary forward
                if map[S[right]] >= 0:
                    count += 1 #only to count those contained in T

                #right boundary already satisfy containing T, now push the left boundary
                while count == len(T):
                    if S[left] in map:
                        map[S[left]] += 1
                        #in this case, cannot push forward anymore
                        if map[S[left]] > 0:
                            #update the minimum length
                            if right - left + 1 < windowLen:
                                windowLen = right - left + 1
                                res = S[left: right+1]
                            count -= 1
                    #push the left boundary
                    left += 1
            right += 1
        return res

print(Solution().minWindow("naxfhghkfburgtekziyvbidfkiaqjvqxynefulrbnouvhyfijgdkqgsaqsqaqixoxbvronvbdpxkqeszkwlccdcvyuvqcueaxbtlqqptgofwsyxfuihymmtmgqclkinhjivczkxhyddsbczxkjxyvtkdjmqwufdgoaipkfwkkbflfekpniqkdaqmpgijmopcoztbhrlruqfzxrombgxehnrwvbhjpxlgyghfxszrlgqixhwzptfwiyugacprbdxbjehjziakotuncqormuquskcuosmpvjtgqappkszanvn","rleizyawsn"))
