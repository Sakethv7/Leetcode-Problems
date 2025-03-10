class Solution:
    def minOperations(self, nums: List[int]) -> int:
        element_count = {}
        for num in nums:
            element_count[num] = element_count.get(num, 0)+1
        
        total_ops = 0

        for count in element_count.values():
            if count == 1:
                return -1  # It's not possible to make the array empty
            total_ops += ceil(count/3)

        return total_ops