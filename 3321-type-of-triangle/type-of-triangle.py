class Solution:
    def triangleType(self, nums: List[int]) -> str:
        #nums size 3if all sides are equal- equi, if exactly 2sides are equal, isosceles, if all sides are of different lenght scalene, return a string, or none
        sum_2_sides =0
        if len(nums) != 3:
            return None
        nums.sort()
      # Check if it forms a valid triangle
        if nums[0] + nums[1] <= nums[2]:
            return "none"  # Not a valid triangle
        if nums[0] == nums[1] == nums[2]:
            return ("equilateral")
        elif nums[0]== nums[1] or nums[0] == nums[2] or nums[1] == nums[2]:
            return ("isosceles")
        else:
            return ("scalene")
         