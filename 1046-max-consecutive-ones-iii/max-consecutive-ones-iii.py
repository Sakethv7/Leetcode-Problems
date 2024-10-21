
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        num_zeroes = 0
        windowstart = 0
        max_length = 0

        for windowend in range(len(nums)):
            if nums[windowend] == 0:
                num_zeroes +=1
    
            while num_zeroes >k:
                if nums[windowstart] ==0:
                   num_zeroes -=1
                windowstart +=1

            max_length = max(max_length, windowend-windowstart+1)
        
        return max_length

