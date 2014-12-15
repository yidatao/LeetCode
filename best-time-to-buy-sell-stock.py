class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        profit = 0
        lowest_buy = prices[0]
        for i in range(1,len(prices)):
            lowest_buy = min(lowest_buy, prices[i])
            profit = max(profit, prices[i] - lowest_buy)
        return profit