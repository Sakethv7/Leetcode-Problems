class Solution:
    def rob(self, nums: List[int]) -> int:                         
                            # skip the first element and skip the last element
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1])) 

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            newrob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newrob
        
        return rob2