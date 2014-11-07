class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply0(self, num1, num2):
        #well this is cheating
        return str(int(num1)*int(num2))

    def multiply1(self, num1, num2):
        sum = 0
        for i in range(len(num1)-1,-1,-1):
            d1 = int(num1[i])
            carry = 0
            total = 0
            for j in range(len(num2)-1,-1,-1):
                loc = len(num2) - 1 - j
                d2 = int(num2[j])
                s = d1 * d2
                total += ((s % 10) + carry)*(10**loc)
                carry = s // 10
            #don't forget the final carry digit
            total += carry * (10**(loc+1))
            l = len(num1) - 1 - i
            sum += total * (10**l)
        return str(sum)


if __name__ == '__main__':
    print(Solution().multiply0('123','4566'))
    print(Solution().multiply1('123','4566'))