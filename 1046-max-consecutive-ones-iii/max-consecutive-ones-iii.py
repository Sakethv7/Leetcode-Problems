
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        num_zeroes = 0
        window_start = 0
        n = len(nums)
        max_length = 0

        for windowend in range(n):
            if nums[windowend] == 0:  # If encounter a zero, increment the zero count
                num_zeroes +=1
        # Shrink the window until the zero count is within the allowed limit
            while num_zeroes >k:
                if nums[window_start]==0:
                    num_zeroes -=1
                window_start += 1
            
            max_length = max(max_length, windowend - window_start +1)   # Update max_length for the current valid window
        
        return max_length