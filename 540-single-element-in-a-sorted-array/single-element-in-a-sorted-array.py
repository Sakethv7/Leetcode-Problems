# from collections import Counter
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # count = Counter(nums)

        # for num, count in count.items():
        #     if count ==1:
        #         return num  #O(n) time and space 


        #Binary search Tree for O(logn) time:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right-left)//2

            #check mid is within bounds and is unique by checking adjacent elements
            if ((mid -1 < 0 or nums[mid] != nums[mid-1]) and 
            (mid+1 == len(nums) or nums[mid] != nums[mid+1])):
                return nums[mid]
            
            # size of the left side
            left_size = mid -1 if nums[mid-1] == nums[mid] else mid

            #left size is odd, so single element is in the first half
            if left_size %2:
                right = mid - 1
            else:
                left = mid + 1
        return -1


