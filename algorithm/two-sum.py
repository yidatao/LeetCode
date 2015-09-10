class Solution:
    #simple solution
    #use a map <value, index>
    #duplicate values are not a problem. If two duplicates' sum equal to target, their indices are returned before value is over-written in the map
    #if not, then over-written is okay
    def twoSum0(self, num, target):
        map = {}
        for i in range(len(num)):
            val = num[i]
            if target-val in map:
                return (map[target-val]+1,i+1)
            map[val] = i

    # @return a tuple, (index1, index2)
    def twoSum1(self, num, target):
        num_reverse = sorted(num,reverse=True)
        #remember the indices of the original array after sorted
        indices = sorted(range(len(num)), key=lambda k: num[k],reverse=True)
        start = 0
        end = len(num)-1
        while start < end:
            sum = num_reverse[start] + num_reverse[end]
            if sum == target:
                index1 = indices[start]+1
                index2 = indices[end]+1
                return (index1,index2) if index1 < index2 else (index2,index1)
            elif sum > target:
                start += 1
            else:
                end -= 1


print(Solution().twoSum0([0,4,3,0],0))