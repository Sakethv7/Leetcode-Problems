class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        #width ramp nums[i]<= nums[j] is j-1

        # return max width of a ramp in nums, if no ramp in nums is 0 

        stack = [] # create a decreasing stack of indices for us

        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        max_width = 0
        for j in range(len(nums)-1, -1, -1):
            while stack and nums[j]>= nums[stack[-1]]:
                i = stack.pop()
                max_width = max(max_width, j-i)
        
        return max_width