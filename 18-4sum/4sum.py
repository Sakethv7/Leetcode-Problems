class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Sort array to handle duplicates and use two pointers
        result = []
        n = len(nums)
        
        # Fix first two numbers and use two pointers for the remaining two
        for i in range(n - 3):
            # Skip duplicates for first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            for j in range(i + 1, n - 2):
                # Skip duplicates for second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Use two pointers for the remaining two numbers
                left = j + 1
                right = n - 1
                
                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if curr_sum == target: # compare current sum 
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates for third number
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicates for fourth number
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                            
                        left += 1 #move the pointer ahead
                        right -= 1 #decrement the pointer
                    elif curr_sum < target:
                        left += 1
                    else:
                        right -= 1
        
        return result