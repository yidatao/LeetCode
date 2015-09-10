class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n <= 1: return 0
        isPrime = [True for x in range(n)]
        isPrime[0],isPrime[1] = False, False
        x = 2
        while x*x < n:
            if isPrime[x]:
                m = x*x
                while m < n:
                    isPrime[m] = False
                    m += x
            x += 1
        return sum(isPrime) #number of True elements in the list