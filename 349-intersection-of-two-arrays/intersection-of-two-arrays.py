class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert both lists to sets to remove duplicates
        # and allow efficient O(1) average lookup time.
        #
        # Use set intersection (&) to get all elements
        # that appear in both sets.
        result = list(set(nums1) & set(nums2))
        
        # Convert the resulting set back to a list and return it.
        return result