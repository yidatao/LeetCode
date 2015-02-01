class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    # Refer to http://www.cnblogs.com/zuoyuan/p/3782107.html
    def fullJustify(self, words, L):
        res = []
        i = 0
        while i < len(words):
            length = 0
            start = i
            #Greedy to find the maximum # of words in a row
            while i < len(words):
                #the last word in a row has no space followed up, otherwise +1 for the space
                l = len(words[i]) if length == 0 else length + 1 + len(words[i])
                if l <= L:
                    length = l
                else:
                    break
                i += 1
            #check pad spaces
            spaceCount = L - length
            slotSpace = 0
            if i - start - 1 > 0 and i < len(words):
                slotSpace = spaceCount / (i - start - 1)
                spaceCount = spaceCount % (i - start - 1)
            #form strings
            s = words[start]
            j = start + 1
            while j < i:
                s += ' '*(slotSpace + 1) # +1 for original one space
                #pad the remaining space evenly
                if spaceCount > 0 and i < len(words):
                    s += ' '
                    spaceCount -= 1
                s += words[j]
                j += 1
            s += ' '*spaceCount #left adjust the last line
            res.append(s)
        return res