import re
class Solution:
    # @return a boolean
    # time limit exceeded
    def isInterleave0(self, s1, s2, s3):
        if sorted(s1+s2) != sorted(s3):
            return False
        indice1 = []
        indice2 = []
        #In s3, find all occurrences of each character in s1/s2
        for c in s1:
            l = [m.start() for m in re.finditer(c, s3)]
            indice1.append(l)
        for c in s2:
            l = [m.start() for m in re.finditer(c, s3)]
            indice2.append(l)
        valid1 = self.getValid(indice1)
        valid2 = self.getValid(indice2)
        allindice = range(len(s3))
        for v in valid1:
            #see if they have complementary indices
            v2 = [item for item in allindice if item not in v]
            if v2 in valid2:
                return True
        return False

    #get valid indices
    def getValid(self, l):
        res = []
        for i in range(len(l)):
            sublist = l[i]
            if i == 0:
                for sl in sublist:
                    res.append([sl])
            else:
                tmp = list(res)
                for sr in tmp:
                    for sl in sublist:
                        #valid if it's increasing
                        if sl > sr[-1]:
                            res.append(sr + [sl])
                        else:
                            break
        #return all valid indices
        return [x for x in res if len(x) == len(l)]

    #Dynamic programming
    #Inspired by http://www.cnblogs.com/zuoyuan/p/3767650.html and the DP matrix from http://blog.csdn.net/u011095253/article/details/9248073
    def isInterleave1(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        #be careful when initialize matrix, the row and column number should be correct
        matrix = [[False for i in range(len(s2)+1)] for j in range(len(s1)+1)]
        #this is a dummy one. So be careful with the index later
        matrix[0][0] = True
        #initialize the edge
        #s2 = "", the problem becomes whether s1 equals to s3
        for i in range(1,len(s1)+1):
            #True if its previous substring is true and its current character equals to s3's current character
            matrix[i][0] = matrix[i-1][0] and s1[i-1] == s3[i-1]
        #s1 = "", similarly
        for j in range(1,len(s2)+1):
            matrix[0][j] = matrix[0][j-1] and s2[j-1] == s3[j-1]
        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                matrix[i][j] = matrix[i][j-1] and s2[j-1] == s3[i+j-1] or matrix[i-1][j] and s1[i-1] == s3[i+j-1]
        return matrix[len(s1)][len(s2)]

print(Solution().isInterleave1('cacccaa','acccaacabbbab','accccaaaccccabbaabab'))