class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s =[]
        next_greater_map ={}

        for num in nums2:
            while s and s[-1]< num:
                next_greater_map[s.pop()] = num
            s.append(num)

        return [next_greater_map.get(num, -1) for num in nums1]     