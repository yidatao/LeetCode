import math
class Solution:
    # @return a string
    def getPermutation(self, n, k):
        res = ''
        k = k - 1
        array = [x for x in range(1, n+1)]
        #factorial result for (n-1)!
        fac = 1
        for x in range(1, n):
            fac *= x

        for i in range(n-1, -1, -1):
            #use pop() to also remove the element from array
            res += str(array.pop(k/fac))
            if i > 0:
                #update k and factorial
                k = k % fac
                fac = fac / i
        return res


print(Solution().getPermutation(3,3))