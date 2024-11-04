class Solution:
    def jump(self, nums: List[int]) -> int:
        #nums[0], forward jump = num[i]
        #return min number of jumps to reach nums[n-1], count basically

            if len(nums)==1:
                return 0

            jumps = 0
            current_end = 0
            farthest = 0

            for i in range(len(nums)):
                farthest = max(farthest, i+nums[i])

                if i == current_end:
                    jumps+=1
                    current_end = farthest

                if current_end >= len(nums)-1:
                    break
            
            return jumps