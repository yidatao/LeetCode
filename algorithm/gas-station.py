class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    # O(N^2), time limit exceeded
    def canCompleteCircuit0(self, gas, cost):
        N = len(gas)
        remain = 0
        # ith starting station
        for i in range(N):
            seq = [x for x in range(i,N)] + [x for x in range(i)]
            #start from i, travel a circle
            count = 0
            for j in seq:
                if remain + gas[j] >= cost[j]:
                    remain = remain + gas[j] - cost[j]
                    count += 1
                else:
                    break
            if count == N:
                return i
        return -1

    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        N = len(gas)
        #the remaining gas
        remain = 0
        #the starting station
        start = 0
        for i in range(N):
            if remain + gas[i] >= cost[i]:
                remain += gas[i] - cost[i]
            else:
                #in this case, cannot get from station i to i+1
                #so we can simply re-start the search from station i+1
                #since any station k between start and i also cannot work, why?
                #because the car can go from start to i implies that the car has at least 0 gas when arriving at each station k inbetween
                #Now if we starts from k (start<=k<i), the remaining gas always starts at zero (equal or even less gas)
                #meaning that it also cannot reach from station i to i+1
                #so, we might as well start from i+1
                remain = 0
                start = i+1
        #since the first line ensures that sum(gas) - sum(cost) >= 0
        #0 to start-1 do not satisfy, since sum(gas)[0 to start-1] - cost(gas)[0 to start-1] < 0
        #so definitely sum(gas)[start to n] - cost(gas)[start to n] + (sum(gas)[0 to start-1] - cost(gas)[0 to start-1]) >= 0 according to the first condition
        #meaning the gas can travel the circle
        return start

print(Solution().canCompleteCircuit([4],[3]))