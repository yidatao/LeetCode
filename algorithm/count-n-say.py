class Solution:
    def generate(self, num):
        next = []
        count = 0
        current = num[0]
        for i in num:
            if i == current:
                count += 1
            else:
                next.append(count)
                next.append(current)
                current = i
                count = 1
        next.append(count)
        next.append(current)
        return next
        
    # @return a string
    def countAndSay(self, n):
        x = [1]
        for i in range(0,n-1):
            x = self.generate(x)
        return ''.join(str(i) for i in x)

if __name__ == '__main__':
    print(Solution().countAndSay(7))