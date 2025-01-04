class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
    
            # When the slow and fast pointers meet, a cycle is detected
            if slow == fast:   
                break
        
        slow2 = 0
        while True:
             # Move both slow and slow2 pointers one step at a time
            slow = nums[slow]
            slow2 = nums[slow2]
             # When slow and slow2 meet, the duplicate number is found
            if slow == slow2:
                return slow