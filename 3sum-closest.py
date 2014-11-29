class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        distance = float("inf") #infinity
        num.sort() #sort the array is the key for efficiency
        res = None
        for i1 in range(len(num)-2):
            a = num[i1]
            if i1 > 0 and a == num[i1-1]:
                #if duplicate value, then move on (for efficiency)
                continue
            i2 = i1+1
            i3 = len(num)-1
            while i2 < i3:
                b = num[i2]
                c = num[i3]
                sum = a+b+c
                if sum == target:
                    return sum
                elif sum < target:
                    if target - sum < distance:
                        distance = target - sum
                        res = sum
                    i2 += 1
                elif sum > target:
                    if sum - target < distance:
                        distance = sum - target
                        res = sum
                    i3 -= 1
        return res

print(Solution().threeSumClosest([-1,2,1,-4],1))