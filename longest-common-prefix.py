class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if strs is None or len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        prefix = strs[0]
        for s in strs[1:]:
            prefix = self.getPrefix(prefix, s)
            if prefix == '':
                break
        return prefix

    def getPrefix(self, str1, str2):
        prefix = ''
        index = 0
        while index < len(str1) and index < len(str2):
            if str1[index] == str2[index]:
                prefix += str1[index]
                index += 1
            else:
                break
        return prefix
