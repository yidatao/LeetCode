class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        map = {}
        longlen, repeat = 0, -1
        for i in range(len(s)):
            #if repeat >= map[s[i]], then no need to update repeat
            #for instance, when meet the second 'z' in the below string,
            #although map['z'] = 0, no need to update repeat since
            #between the two 'z', there are already duplicate chars
            #the latest repeat location is for the first 'c'
            if s[i] in map and repeat < map[s[i]]:
                repeat = map[s[i]]
            longlen = max(longlen, i - repeat)
            map[s[i]] = i

        return longlen

print(Solution().lengthOfLongestSubstring("zwxyabcabczbb"))