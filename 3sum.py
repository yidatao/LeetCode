class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    # this solution exceeds time limit
    def threeSum0(self, num):
        if num is None:
            return []
        res = []
        map = {}
        for i in range(0,len(num)):
            map[num[i]] = i
        for i in range(0,len(num)-1):
            for j in range(i+1,len(num)):
                subsum = num[i]+num[j]
                if -subsum in map and map[-subsum] != i and map[-subsum] != j:
                    list = sorted([num[i],num[j],-subsum])
                    if list not in res:
                        res.append(list)
        return res

    def threeSum1(self, num):
        if num is None:
            return []
        num.sort() #sort the array is the key for efficiency
        res = []
        for i1 in range(len(num)-2):
            a = num[i1]
            if i1>0 and a == num[i1-1]:
                #if duplicate value, then move on (for efficiency)
                continue
            i2 = i1+1
            i3 = len(num)-1
            while i2 < i3:
                b = num[i2]
                c = num[i3]
                if b+c == -a:
                    l = [a,b,c]
                    if l not in res:
                        res.append(l)
                    i2 += 1
                    i3 -= 1
                    #move the index to the next *distinct* value (for efficiency)
                    while i2 < i3 and num[i2] == num[i2-1]:
                        i2 += 1
                    while i2 < i3 and num[i3] == num[i3+1]:
                        i3 -= 1
                elif b+c < -a:
                    i2 += 1
                    #move the index to the next *distinct* value (for efficiency)
                    while i2<i3 and num[i2] == num[i2-1]:
                        i2+=1
                else:
                    i3 -= 1
                    #move the index to the next *distinct* value (for efficiency)
                    while i2<i3 and num[i3] == num[i3+1]:
                        i3 -= 1
        return res

print(Solution().threeSum1([0,0,0,0]))