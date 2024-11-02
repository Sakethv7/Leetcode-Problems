class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
         # Set the binary search range: minimum speed is 1, maximum speed is the largest pile
        left,right = 1, max(piles)
     # Initialize result with the maximum possible speed, which will be minimized in the loop
        res = right
    # Perform binary search to find the minimum eating speed
        while left <=right:
            # Calculate the middle speed value in the current range
            k = (left+right)//2

            hours = 0 #total hours needed to eat all piles at speed k
            for p in piles:
                hours += math.ceil(p/k) 
                # to round of the number math.ceil to ensure all bananas in a pile are eaten in whole hours
            
            if hours <=h: # If the total hours are within the allowed time
                res =min(res, k)   # Update the result with the minimum speed found so far

                right = k-1 #look for lower speed as we need to return minimum. goes to the left half of k range
            else: #when total hours is greater than h, the allowed time
                left =  k+1 # Look for a possibly higher speed to minimize furthe. goes to the right half of the array
        
        return res  # Return the minimum speed that allows eating all piles within h hours