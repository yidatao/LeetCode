class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1: return s
        res = ["" for x in range(nRows)]
        row = 0
        isVertical = True #whether should go down or go up
        for c in s:
            res[row] += c
            if isVertical:
                #if reach the end, then go up
                if row == nRows - 1:
                    row -= 1
                    isVertical = False
                else:
                    row += 1
            else:
                #if reach the first or second row, then should go down
                if row <= 1:
                    isVertical = True
                if row >= 1:
                    row -= 1
                elif row == 0:
                    row += 1
        return "".join(res)

print(Solution().convert("ABCD",2))