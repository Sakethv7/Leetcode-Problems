class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = sum(nums)
        return total % k # the remainder becomes the number of operations required to make it divisible by k
                