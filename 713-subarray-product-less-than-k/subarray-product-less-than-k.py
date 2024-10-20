class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if(k<=1):
            return 0

        n = len(nums)
        count = 0
        product = 1

        start = 0

        for end in range(n):
            product *= nums[end]

            while product >= k and start<=end:
                product = product // nums[start] 
                #In the sliding window approach, we are continuously multiplying the elements of the subarray as we expand the window by moving the end pointer.
                #When the product of the subarray becomes greater than or equal to k, we need to shrink the window by moving the start pointer to the right.
                start +=1
            
            count += end-start+1
        
        return count
