class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        count = 0
        prefix_sum = 0
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1 #intialise 0 for cases where a subarray starting from the beginning 
        # To handle the case where prefix_sum itself equals the goal
       
        for num in nums:
            prefix_sum +=num

            if prefix_sum-goal in prefix_counts: # Check if there is a prefix that makes up the goal
                count+=  prefix_counts[prefix_sum-goal]
            
            prefix_counts[prefix_sum] +=1  # Update the prefix count map
        
        return count
