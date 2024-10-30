class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
# i!=j, j!=k and i!=k. nums[i]+nums[j] + nums[k] ==0, return nums[i, j , k] can 2 , can be 1 array. this is in a list
        #sorted solution

        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n-2):
            # Skip duplicate elements for the first number in the triplet
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i+1, n-1
        # Iterate through each element, using it as the fixed element in the triplet
            while left< right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    ans.append([nums[i], nums[left], nums[right]])
        # Move both pointers to continue searching for new pairs without duplicates
                    left+=1 
                    right -=1
        # Skip duplicate values for the `left` pointer to avoid duplicate triplets
                    while left< right and nums[left]== nums[left-1]:
                        left+=1
        # Skip duplicate values for the `right` pointer to avoid duplicate triplets
                    while left < right and nums[right] == nums[right+1]:
                        right -=1
        
        
                elif current_sum < 0: # If the current sum is less than zero, increment left to increase the sum
                    left+=1
        
                else: # If the current sum is greater than zero, decrement `right` to decrease the sum
                    right -=1

        return ans