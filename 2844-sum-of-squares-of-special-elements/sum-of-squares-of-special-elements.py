class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        # nums[i] is special if n%i == 0
        # return the sum of the squares of all special elements 

        square_sum = 0
        n = len(nums)

        for i in range(n):
            if  n % (i+1) == 0:
                square_sum += nums[i]*nums[i]
            
        return square_sum