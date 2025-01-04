class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i, n = 0, len(nums)

        while i < n:
            j = nums[i]-1

            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != i+1:
                return nums[i]
        
        return -1