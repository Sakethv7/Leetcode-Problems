class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        g_stack = [] # stores indices
        result = [-1] * n # result array

        for i in range(n * 2):
            while g_stack and nums[g_stack[-1]] < nums[i % n]:
                result[g_stack.pop()] = nums[ i% n]
            if i < n:
                g_stack.append(i)
    
        return result
