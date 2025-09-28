class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True) # sort in descending order

        for i in range(len(nums) - 2 ): # Check triples starting from the largest
            a, b, c = nums[i], nums[i+1], nums[i+2]
            
            if b + c > a: # Triangle inequality: sum of smaller two > largest
                return a + b + c

        return 0    


