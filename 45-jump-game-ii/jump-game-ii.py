class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0 # number of jumps
        l = r = 0 # Current range of indices we can jump within

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1): # Find the farthest we can reach within the current range [l, r]
                farthest = max(farthest, i + nums[i])
            l = r + 1 # Move the left bound of the range
            r = farthest # Update the right bound to the farthest point we can reach
            res += 1  # Increment the jump count
        
        return res