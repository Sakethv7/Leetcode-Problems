class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - min_price) #max_profit starts at 0 and only ever gets replaced when prices[i] - min_price is larger than 0 
            min_price = min(min_price, prices[i]) #track minimum price of stock
        return max_profit 