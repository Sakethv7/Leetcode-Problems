class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s =[]# Stack to keep track of numbers for which we are finding the next greater element
        next_greater_map ={} # Dictionary to store the next greater element for each number in nums2

        for num in nums2:
            while s and s[-1]< num: 
            # While there are elements in the stack and the current number is greater than the top of the stack
                next_greater_map[s.pop()] = num # Map the top element to the current number since the current number is the next greater element
            s.append(num)# Push the current number onto the stack
            
        # For each number in nums1, get the next greater element from the map; if not present, return -1
        return [next_greater_map.get(num, -1) for num in nums1]     