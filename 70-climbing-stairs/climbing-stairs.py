class Solution:
    def climbStairs(self, n: int) -> int:
        #return the number of distinct ways you can climb to the top
        # `one` represents the number of ways to reach the current step
        # `two` represents the number of ways to reach the previous step
        one, two = 1, 1

        for i in range(n-1):      # Loop through each step from 1 to n-1
            temp = one
            # Update `one` to represent the number of ways to reach the current step
            # This is the sum of ways to reach the last step (`one`) and the previous step (`two`)
            one = one + two
            two = temp
        
        return one