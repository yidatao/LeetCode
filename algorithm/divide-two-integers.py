import sys
class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        dividend, divisor = abs(dividend), abs(divisor)
        q, d, k = 0, 0, 0
        while dividend >= divisor:
            d = divisor
            k = 1
            #enlarge the divisor to 2*divisor each time
            while d + d <= dividend:
                d += d
                k += k
            dividend -= d
            q += k
        if str(q * sign) == '2147483648': return q - 1
        return q * sign
