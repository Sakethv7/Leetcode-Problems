class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        s = 0
        ans = []

        if n< 3:
            return []
        
        nums.sort()

        for i in range(n-2):
            if i >0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = n-1

            while left< right:
                s = nums[i] + nums[left] + nums[right]

                if s == 0:
                    ans.append((nums[i], nums[left], nums[right]))
                    left += 1
                    right -=1 
                    while nums[left] == nums[left-1] and left<right:
                        left += 1
                    while nums[right] == nums[right+1] and left < right:
                        right -= 1
                elif s<0:
                    left += 1
                else:
                    right -= 1
        
        return ans






