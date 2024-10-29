class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #m is elements in nums1 and n is elements in nums
        #nums1 and nums2 are already sorted asc
        #merge nums1 and nums 2
        # so we need to create m+n array in nums1, so we merge from the end of the array and go on decrementing

        i, j, k = m-1, n-1, m+n-1

     #While there are elements in both nums1 and nums2
        while i>=00 and j>=00:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -=1
            
            elif nums2[j] >= nums1[i]:
                nums1[k] = nums2[j]
                j -=1   
            k-=1
        
         # If there are remaining elements in nums2, add them in nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1