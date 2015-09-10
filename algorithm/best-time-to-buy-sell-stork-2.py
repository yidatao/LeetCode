class Solution:
    # @param prices, a list of integer
    # @return an integer
    # greedy?
    def maxProfit(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            #if day i larger than day i-1, then buy on day i-1 and sell on day i to make profit
            #note that it's okay to sell then buy on the same day
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit