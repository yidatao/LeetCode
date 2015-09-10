class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        res = [0 for x in range(len(digits))]
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            res[i] = (digits[i] + carry) % 10
            carry = (digits[i] + carry) // 10
        if carry > 0:
            res.insert(0, carry)
        return res