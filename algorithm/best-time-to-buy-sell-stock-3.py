class Solution:
    # @param prices, a list of integer
    # @return an integer
    # Time limit exceeded O(n^2)
    def maxProfit0(self, prices):
        profit = 0
        for i in range(len(prices)):
            p1 = self.getMaxProfit(prices[:i])
            p2 = self.getMaxProfit(prices[i:])
            profit = max(profit, p1 + p2)
        return profit

    def getMaxProfit(self, array):
        if len(array) < 2:
            return 0
        profit = 0
        lowest = array[0]
        for i in range(1,len(array)):
            lowest = min(lowest, array[i])
            profit = max(profit, array[i]-lowest)
        return profit

    def maxProfit1(self, prices):
        if len(prices) < 2:
            return 0
        #profit[i] is the max profit got from 1 transaction in range [0,i] (same as problem I)
        profits = [0 for x in range(len(prices))]
        lowest = prices[0]
        maxProfit = 0
        for i in range(len(prices)):
            lowest = min(lowest, prices[i])
            maxProfit = max(maxProfit, prices[i]-lowest)
            profits[i] = maxProfit

        #check the max profit from the last element of prices backwards [n-1 backwards to i] (since we can buy and sell on the same day)
        #since backwards, use highest instead of lowest (but the idea is the same)
        highest = prices[-1]
        res = profits[-1]
        for i in range(len(prices)-1,-1,-1):
            highest = max(highest, prices[i])
            #here, profit is the max profit obtained from one transaction in range[i,n-1]
            profit = highest - prices[i]
            #as the globally max profit, add the max profit obtained from one transaction in range[i,n-1] to the max profit got from 1 transaction in range [0,i]
            res = max(res, profit + profits[i])
        return res

print(Solution().maxProfit1([2,1,2,0,1]))