class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        

        while left <= right:
            if nums[left] > nums[right]:
                left += 1
            elif nums[left]< nums[right]:
                right -= 1
            
            if left == right:
                return nums[left]


