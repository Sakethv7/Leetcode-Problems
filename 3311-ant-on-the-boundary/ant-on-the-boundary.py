class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        
        #sum += nums[i]
        #if diff ==0: count +=1
        sum = 0
        count = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum == 0:
                count +=1
        
        return count