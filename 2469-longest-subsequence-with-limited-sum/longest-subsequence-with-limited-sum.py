from typing import List
from bisect import bisect_right

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort() #sort the nums array
        prefix_arr = [0]*len(nums) # create a prefix sum array and fill it 
        prefix_arr[0] = nums[0]
 
        for i in range(1, len(nums)):  # fill it by adding prefix sum elements by adding nums[i] to prefix_arr[0]
            prefix_arr[i] = prefix_arr[i-1] + nums[i]
        
        # Process each query and find the upper bound
        ans = []
        for query in queries:
            # Use bisect_right to find the position where query fits in prefix_arr
            count_nums = bisect_right(prefix_arr, query) #bisect returns the position of the iterator or the number of elements required to make a longest subsequence for the sum
            ans.append(count_nums)
        
        return ans