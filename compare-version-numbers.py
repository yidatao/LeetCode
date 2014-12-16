class Solution:
    # @param a, a string
    # @param b, a string
    # @return a boolean
    def compareVersion(self, version1, version2):
        v1 = [int(x) for x in version1.split('.')]
        v2 = [int(x) for x in version2.split('.')]
        i = 0
        #Note there could be multiple dots in a version number
        while i < len(v1) and i < len(v2):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
            i += 1
        if i == len(v1):
            for j in range(i,len(v2)):
                if v2[j] > 0:
                    return -1
        elif i == len(v2):
            for j in range(i,len(v1)):
                if v1[j] > 0:
                    return 1
        return 0


