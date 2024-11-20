class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # return the kth integer missing from this array- already sorted array, k is the index of the missing number

        # can we use binary search? take a mid point? if the number is bigger

        # o(logn)

        n = len(arr)
        left, right = 0, n-1

        while left<=right:

            mid = (left+right)//2

            missing = arr[mid] - (mid + 1) #number of missing integers before arr[mid]

            if missing < k:
                left = mid+1
            else:
                right = mid-1

        
        return k+left

