class Solution:
    # @return an integer
    def lengthOfLongestSubstring0(self, s):
        map = {}
        #repeat is the most recent location where a duplicate happens
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

    # @return an integer
    # TLE
    def lengthOfLongestSubstring0(self, s):
        if s is None or len(s) == 0: return 0

        array = [1 for x in range(len(s))]

        for i in range(0, len(s)-1):
            for j in range(i+1, len(s)):
                if s[j] not in s[i:j]:
                    array[i] += 1
                else:
                    break
        return max(array)


    def lengthOfLongestSubstring(self, s):
        if s is None or len(s) == 0: return 0
        map = {}
        map[s[0]] = 0
        #dp[i] is the length of longest substring that ends with s[i]
        dp = [1 for x in range(len(s))]
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                if s[i] not in map:
                    dp[i] = dp[i-1] + 1
                elif map[s[i]] < i - dp[i-1]:
                    #if s[i] already appears, but outside the longest substring that ends at i-1, then it doesn't matter
                    dp[i] = dp[i-1] + 1
                else:
                    #if s[i] appears inside the longest substring that ends at i-1, then we need to re-calculate the length
                    dp[i] = i - map[s[i]]
            #update the most recent index of each character
            map[s[i]] = i
        return max(dp)

print(Solution().lengthOfLongestSubstring("zwxyabcabczbb"))