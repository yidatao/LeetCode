class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits0(self, n):
        binary = bin(n)[2:].zfill(32)
        reverse = str(binary)[::-1]
        return int(reverse, 2)

    def reverseBits(self, n):
        binary = self.intToBinary(n)
        binary32 = "0"*(32-len(binary))+binary
        return self.binToInt(binary32[::-1])


    def intToBinary(self, n):
        b = ""
        while n > 0:
            bit = n % 2
            b = str(bit) + b
            n = n / 2
        return b

    def binToInt(self, binStr):
        res = 0
        power = 0
        for i in binStr[::-1]:
            res += int(i) * (2 ** power)
            power += 1
        return res

print(Solution().reverseBits(1))