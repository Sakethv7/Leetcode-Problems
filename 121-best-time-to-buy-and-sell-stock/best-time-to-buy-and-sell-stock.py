class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we need to return maximum profit which is the difference of 2 values in the array prices
        maxprofit = 0
        cheapest_price = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < cheapest_price:
                cheapest_price = prices[i]
            
            elif prices[i] > cheapest_price:
                profit = prices[i] - cheapest_price
                maxprofit =  max(maxprofit, profit)
        

        if maxprofit == 0:
            return 0
        
        else:
            return maxprofit
        


            