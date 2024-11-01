class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search- O(logn)
        #if nums[target] in nums[left] : return target ese return -1

        # find a middle element, search the target on the left side and right side. nums[mid]<nums[mid-1]: left+1

        left, right = 0, len(nums)-1

        while left<=right:
            mid = (left+right )//2 #find the middle element from which we can check which half left or right is sorted
 
            if nums[mid] == target: # Check if the mid element is the target
                return mid

            # Determine which half is sorted
            if nums[left] <= nums[mid]:  # Left half is sorted
                if nums[left] <= target < nums[mid]:  # Target is in the left half
                    right = mid - 1
                else:  # Target is in the right half
                    left = mid + 1
            else:  # Right half is sorted
                if nums[mid] < target <= nums[right]:  # Target is in the right half
                    left = mid + 1
                else:  # Target is in the left half
                    right = mid - 1
        return -1