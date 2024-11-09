class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quadriples = []
        nums.sort()
        n = len(nums)

        for i in range(n-3):
            if i>0 and nums[i]== nums[i-1]:   # Skip duplicates for i
                continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]: # Skip duplicates for j
                    continue
                self.findquad(nums, target, i, j, quadriples) # Call the helper method with proper self reference
    
        return quadriples

    def findquad(self, nums, target, first, second, quadriples):

        left = second+1
        right = len(nums) -1

        while left < right:
            quad_sum = nums[first] + nums[second] + nums[left] + nums[right]

            if quad_sum == target:
                quadriples.append([nums[first], nums[second], nums[left], nums[right]]) # Append as a list

                left +=1
                right-=1

                while left < right and nums[left] == nums[left-1]:   # Skip duplicates
                    left += 1
                while left< right and nums[right] == nums[right+1]:   # Skip duplicates
                    right -= 1
            elif quad_sum < target:
                left += 1
            elif quad_sum > target:
                right -= 1
            