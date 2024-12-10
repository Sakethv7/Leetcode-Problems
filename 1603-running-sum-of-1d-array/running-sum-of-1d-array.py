class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        #runingsum[i] = sum(nums[0]... nums[i])

        #sum = nums[0]
        #runningsum[i] += sum + nums[i-1]
        #sum = nums[i]

        runningsum = [0]*len(nums)
        runningsum[0] = nums[0]
        sum = nums[0]

        for i in range(1, len(nums)):
            runningsum[i] = sum + nums[i]
            sum = runningsum[i]
        
        return runningsum
