class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        buy = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            curr_profit = prices[i]-buy
            if curr_profit > max_profit:
                max_profit = curr_profit
            if prices[i] < buy:
                buy = prices[i]
        return max_profit