class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        positive_count, negative_count, max_length = 0, 0, 0

        for num in nums:
            if num > 0:
                positive_count = positive_count + 1
                negative_count = negative_count + 1 if negative_count > 0 else 0
            elif num < 0:

                positive_count, negative_count = negative_count + 1 if negative_count > 0 else 0, positive_count + 1
            
            else:
                positive_count = 0
                negative_count = 0 #if num = 0, reset the counters
            
            max_length = max(max_length, positive_count)
        
        return max_length



