class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-1

        while left < n-1 and nums[left] <= nums[left+1]: # Find the first element from the left that is out of order
            left +=1
        
        if left == n-1: # If the array is already sorted
            return 0
        
        while right > 0 and nums[right] >= nums[right-1]:   # Find the first element from the right that is out of order
            right -= 1
        
        subarray_min = min(nums[left:right +1])
        subarray_max = max(nums[left:right +1])

        while left > 0 and nums[left-1] > subarray_min: # Expand the left boundary to include any out-of-place elements
            left -= 1
        
        while right < n-1 and nums[right + 1] < subarray_max:  
            # Expand the right boundary to include any out-of-place elements
            right += 1
        
        return right - left + 1 # return length of the shortest subarray