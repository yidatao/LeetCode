class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        res = 0
        stack = []
        for i in range(len(s)):
            #found a match
            if s[i] == ')' and len(stack) > 0 and s[stack[-1]] == '(':
                stack.pop()
                #if stack is empty, meaning all parentheses before index i are matched.
                #so the longest valid substring should have length i+1
                if len(stack) == 0:
                    #no need to compute max, since i+1 itself is the maximum length so far
                    res = i+1
                else:
                    #update the max length
                    res = max(res, i - stack[-1])
            else:
                #push the INDEX to the stack
                stack.append(i)
        return res

print(Solution().longestValidParentheses(')())(())'))
