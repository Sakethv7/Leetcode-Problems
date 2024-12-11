class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = prices[:]
        n = len(prices)
        stack = []

        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:  # The price at the index on top of the stack is greater than or equal to the current price (prices[i]). This means the current price can serve as a discount.
                index = stack.pop()
                answer[index] -= prices[i]
            
            stack.append(i)
        
        return answer
        # #O(n^2) method
        # for i in range(n):
        #     discount = 0
        #     for j in range(i+1, n):
        #         if prices[j] <= prices[i]:
        #             discount = prices[j]
        #             break
            
        #     answer.append(prices[i]-discount)
        
        # return answer

