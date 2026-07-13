class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {} #dictionary

        for i, x in enumerate(nums):
            complement = target - x
            if complement in prevmap:
                return [prevmap[complement], i]
            prevmap[x] = i
        
        return 