class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeroes_count =0
        max_length =0
        windowstart =0

        for windowend in range(len(nums)):
            if(nums[windowend]==0):
                zeroes_count+=1 #count number of zeroes in the array
            
            while zeroes_count >1:
                if nums[windowstart] ==0:
                    zeroes_count -=1
                
                windowstart +=1
            
            max_length = max(max_length, windowend -windowstart +1-1) 
            # We subtract one from the window length because we need to delete one element
        
        return max_length