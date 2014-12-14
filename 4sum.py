class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    # simply reuse 3sum, but exceeds time limit O(n^3)
    def fourSum0(self, num, target):
        if num is None:
            return []
        num.sort() #sort the array is the key for efficiency
        result = []
        for i in range(len(num)-3):
            a = num[i]
            if i > 0 and a == num[i-1]:
                continue
            res = self.threeSum(num[i+1:], target-a)
            for r in res:
                list = r + [a]
                if list not in result:
                    result.append(sorted(list))
        return result


    def threeSum(self, num, target):
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
                if b+c == target-a:
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
                elif b+c < target-a:
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

    def fourSum1(self, num, target):
        res = []
        map = {} # <sum of two, list of (index1, index2)>
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                s = num[i] + num[j]
                if s in map:
                    map[s].append((i,j))
                else:
                    map[s] = [(i,j)]
        for k,v in map.items():
            if target - k in map:
                v2 = map[target-k]
                for elem1 in v:
                    for elem2 in v2:
                        l = set()
                        for i in [0,1]:
                            l.add(elem1[i])
                            l.add(elem2[i])
                        #check if there are four different indices
                        if len(l) == 4:
                            value = []
                            for elem in l:
                                value.append(num[elem])
                            if sorted(value) not in res:
                                res.append(sorted(value))
        return res


print(Solution().fourSum1([1,0,-1,0,-2,2],0))