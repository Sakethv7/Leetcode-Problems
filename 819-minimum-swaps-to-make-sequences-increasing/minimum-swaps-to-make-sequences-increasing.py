class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        # Initialize the number of swaps when not swapping or swapping the i-th element
        no_swap, swap = 0, 1
      
        for i in range(1, len(nums1)): # Iterate over arrays starting from the second element (index 1)
            no_swap_cost, swap_cost = no_swap, swap
            
            if nums1[i - 1] >= nums1[i] or nums2[i - 1] >= nums2[i]:
                # If the current pair or the previous pair is not strictly increasing,
                no_swap, swap = swap_cost, no_swap_cost + 1  # we must swap this pair to make the sequence increasing

            else: # If it is strictly increasing, no need to swap the previous pair
                swap = swap_cost + 1  # We can choose to swap the current pair
                # If swapping makes both arrays increasing,
                # consider minimum swaps by either swapping or not swapping previous pairs
                if nums1[i - 1] < nums2[i] and nums2[i - 1] < nums1[i]:
                    no_swap, swap = min(no_swap, swap_cost), min(swap, no_swap_cost + 1)
      
        
        return min(no_swap, swap) # Return the minimum number of swaps to make both arrays strictly increasings