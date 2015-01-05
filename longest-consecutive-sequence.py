class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        visited = {x:False for x in num}
        longest = 0
        for x in num:
            #process only if x hasn't been visited
            if not visited[x]:
                visited[x] = True
                seq_len = 1
                #explore larger consecutive numbers
                pivot = x+1
                #stop until the number is not in num
                while pivot in visited:
                    visited[pivot] = True
                    seq_len += 1
                    pivot += 1
                #explore smaller consecutive numbers
                pivot = x-1
                while pivot in visited:
                    visited[pivot] = True
                    seq_len += 1
                    pivot -= 1
                #update the longest sequence so far
                longest = max(longest, seq_len)
        return longest

print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
