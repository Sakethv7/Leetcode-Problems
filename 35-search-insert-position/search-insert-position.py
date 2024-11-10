class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #o(logn ) time means binary search
        # mid = left+right//2, if nums[mid]> target, left = mid+1, if nums[mid]< target, right = mid-1

        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid  # target found at index mid

        # If target is not found, left will be the insertion point
        return left