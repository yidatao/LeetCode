class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        if haystack is None:
            return -1
        if needle == "":
            return 0
        if haystack == "":
            return -1
            
        i, j, p = 0, 0, 0
        match = False
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                #if previous has no match, remember the next location of i to start if future mismatch happens
                if not match:
                    match = True
                    p = i
            else:
                #if currently in match state, reset i to p as the next location to explore. Otherwise simply increase i
                i = p if match else i+1
                j = 0
                match = False
        return i - len(needle) if j == len(needle) else -1

print(Solution().strStr("mississippi","issip"))