class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #o(logn) time and search means binary search algorithm
        #peak element is strictly greater than its neighbors, even if the endpoint does not have neighbours
        # any adjacent elements would not be equal nums[i] != nums[i + 1] for all valid i.
        #graphically points monotonicaly increase, so we need to take a modified binary search approach
        #or maybe it is increasing to decreasing, in a decreasing function, forces us to choose a modified binary search approach
        #once we calculate mid, we check if mid is the peak, if not then we check which neighbour is larger, then in that neighbour's direction we search
        
        #logn time o(1) constant memory
        left, right = 0, len(nums)-1
        while left <=right:
            mid = left + ((right - left)//2) #integer division, finding the middle element of the array
            #check if left neighbor greater
            if mid >0 and nums[mid]< nums[mid-1]:
                right = mid - 1
            #check if right neighbor greater (also checking if mid is not greater than the length of the array)
            elif mid < len(nums)-1 and nums[mid] < nums[mid+1]:
                left = mid+1

            else:
                return mid

           
