class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        map = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in map:
                if len(stack) == 0 or stack[-1] != map[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return True if len(stack)==0 else False