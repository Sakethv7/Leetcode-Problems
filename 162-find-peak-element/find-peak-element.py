class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        while left < right:
            mid = (left+right)//2
            if nums[mid]< nums[mid+1]:
                left = mid+1
            else:
                right = mid #peak is at left half of the array
        
        return left # when left == right then peak is found so we can return left for peak's index
