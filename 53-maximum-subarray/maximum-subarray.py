class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Initialize current sum and max sum with the first element
        current_sum = max_sum = nums[0]

        # Iterate from the second element onwards
        for num in nums[1:]:
            # Update current_sum by considering either the current element alone 
            # or extending the current subarray by adding the num in nums
            current_sum = max(num, current_sum + num)

            # Update max_sum if current sum is larger
            max_sum = max(max_sum, current_sum)

        return max_sum