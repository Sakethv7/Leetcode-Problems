class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # we need to search both left and right side of the array
        # find mid point of the array, compare the middle number to the target, if it is more than the target
        # then bring the right pointer to mid-1, if mid number is less than target, bring left to mid +1
        # if it is equal to target then return mid, else return -1, o(logn), O(1) time and space

        left, right = 0, len(nums)-1

        while left<=right:
            mid = (left+right)//2
            if nums[mid]> target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
            elif nums[mid] == target:
                return mid
                
        return -1
