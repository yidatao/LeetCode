import collections
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    # Reference: http://www.cnblogs.com/zuoyuan/p/3697045.html
    def findLadders(self, start, end, dict):
        map = {}
        for w in dict:
            map[w] = []
        alphabet = [chr(ord('a') + x) for x in range(26)]
        curr = set(); curr.add(start)
        wordLen = len(start)
        while True:
            prev = curr
            curr = set()
            for word in prev:
                dict.remove(word)

            for word in prev:
                for i in range(wordLen):
                    p1, p2 = word[:i], word[i+1:]
                    for j in alphabet:
                        if j != word[i]:
                            #get all possible transformations using alphabet
                            newWord = p1 + j + p2
                            if newWord in dict:
                                #key is the word AFTER transformation, value is the list of valid words BEFORE transformation
                                map[newWord].append(word)
                                curr.add(newWord)
            #no valid transformation
            if len(curr) == 0: return []
            if end in curr: break

        res = []
        self.buildpath([], end, map, res)
        return res

    #recover all valid paths from the map
    def buildpath(self, path, word, map, res):
        if len(map[word])==0:
            path.append(word)
            currPath = list(path)
            currPath.reverse()
            res.append(currPath)
            path.pop()
            return
        path.append(word)
        for v in map[word]:
            self.buildpath(path, v, map, res)
        path.pop()

print(Solution().findLadders('a','c',set(['a','b','c'])))