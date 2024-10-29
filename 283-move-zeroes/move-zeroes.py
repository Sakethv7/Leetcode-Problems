class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0 
        for right in range(len(nums)):
            if nums[right] != 0: 
    #right pointer iterates through the list of nums. if its a non zero element, it will swap and increment left+=1
                nums[left], nums[right] = nums[right], nums[left]
                left +=1