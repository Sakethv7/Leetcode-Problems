class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        closest_sum = 0 #inititliazing a closest sum
        diff = float('inf') # initializing a min_difference variable 
 # using 3 pointers 
        for i in range(n-2):
            left, right = i+1, n-1
            while(left< right):
                curr_sum = nums[i] + nums[left]+ nums[right]
                curr_diff= abs(curr_sum - target)

                if curr_diff < diff or curr_diff == diff :
                    closest_sum = curr_sum
                    diff= curr_diff
                
                if curr_sum< target:
                    left+=1
                else:
                    right-=1
        
        return closest_sum

        