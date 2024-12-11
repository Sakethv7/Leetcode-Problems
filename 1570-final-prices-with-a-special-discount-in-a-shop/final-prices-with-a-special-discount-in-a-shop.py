class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []
        n = len(prices)
        
        for i in range(n):
            discount = 0
            for j in range(i+1, n):
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break
            
            answer.append(prices[i]-discount)
        
        return answer