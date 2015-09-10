import collections
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    # BFS: reference http://chaoren.is-programmer.com/posts/43039
    def ladderLength(self, start, end, dict):
        dict.add(end)
        alphabet = [chr(ord('a') + x) for x in range(26)]
        #use double-ended queue for speed
        queue = collections.deque([(start, 1)])
        wordLen = len(start)
        while queue:
            node = queue.popleft()
            word = node[0]
            step = node[1]
            if word == end:
                return step
            for i in range(wordLen):
                p1, p2 = word[:i], word[i+1:]
                for j in alphabet:
                    if j != word[i]:
                        #get all possible transformations using alphabet (<- BFS) and check if it's in the dict
                        newWord = p1 + j + p2
                        if newWord in dict:
                            queue.append((newWord, step + 1))
                            dict.remove(newWord)
        return 0