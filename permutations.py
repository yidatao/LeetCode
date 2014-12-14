class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    # Inspired by subsets problem
    def permute0(self, num):
        res = []
        self.dfs(num,0,res)
        #here is not elegant, sinc the results also have permutations of all subsets
        return [x for x in res if len(x) == len(num)]

    def dfs(self, array, i, res):
        if i == len(array):
            res.append([])
        else:
            self.dfs(array, i+1, res)
            tmp = list(res) #note to copy
            for item in tmp:
                #insert array[i] to every position of a list
                #e.g., insert 1 to [2,3] at position 0,1,2
                for k in range(len(item)+1):
                    t = list(item) #note to copy
                    t.insert(k,array[i])
                    res.append(t)

    def permute1(self, num):
        if len(num) <= 1:
            return [num]
        res = []
        #isolate the last element num[-1], insert it to each position of all permutations of the remaining elements num[:-1]
        for item in self.permute1(num[:-1]):
            #here the for loop means all insertion positions (similar to dfs())
            res += [item[:i] + [num[-1]] + item[i:] for i in range(len(item)+1)]
        return res

print(Solution().permute1([1,2,3]))