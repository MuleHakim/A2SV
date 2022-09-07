class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        sell, prev_sell = 0, 0
        buy, prev_buy = -prices[0], 0
        for price in prices:
            prev_buy = buy
            buy = max(prev_sell-price, prev_buy)
            prev_sell = sell
            sell = max(prev_buy+price, prev_sell)
        return sell