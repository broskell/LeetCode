class Solution(object):
    def maxProfit(self, prices):
        mini = prices[0]
        profit = 0

        # Brute Force
        # for i in range(1, len(prices), +1):
        #     if prices[i] < mini:
        #         mini = prices[i]
        #     for j in range(i + 1, len(prices), +1):
        #         if prices[i] - mini > profit:
        #             profit = prices[i] - mini
        # return profit
        
        # Optimal
        for i in range(1, len(prices), +1):
            if prices[i] < mini:
                mini = prices[i]
            if prices[i] - mini > profit:
                profit = prices[i] - mini
        return profit