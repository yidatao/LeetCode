class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        res = ''
        l = min(len(a), len(b))
        a, b = a[::-1], b[::-1]
        count = 0
        for i in range(l):
            s = int(a[i]) + int(b[i]) + count
            res += str(s % 2)
            count = s / 2
        rest = a[l:] if len(a) > len(b) else b[l:]
        for c in rest:
            s = int(c) + count
            res += str(s % 2)
            count = s / 2
        if count > 0:
            res += str(count)
        return res[::-1]