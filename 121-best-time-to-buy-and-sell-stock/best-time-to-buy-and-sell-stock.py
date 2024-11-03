class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #ith day, prices[i] is the price of a given stock
        #maximize profit by choosing a single day to buy and sell it on a different day 
        #return max profit, if no profit return 0

        #[7,1,5,3,6,4] output 5 buy in day 2 and sell on day 5 profit 6-1 = 5
        #abosulute of profit - diff = 

        max_profit = 0
        cheapest_price = prices[0]

        for i in range(1, len(prices)):
            if cheapest_price > prices[i]:
                cheapest_price = prices[i]
            else:
                profit = prices[i] - cheapest_price
                max_profit = max(max_profit, profit)

        return max_profit
