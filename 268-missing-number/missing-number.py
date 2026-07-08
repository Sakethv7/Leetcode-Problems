class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashset = set(nums)
        rng = len(nums)+1

        for number in range(rng):
            if number not in hashset:
                return number
