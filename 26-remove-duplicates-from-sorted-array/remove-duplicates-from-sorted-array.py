class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #remove duplicates, order should be same. return the unique element array, and return k- number of unique elements
        #first k elements of the array contain unique elements in ascending order. 

        # [1,1,2] -> [1,2,1] k =2 , [0,0,1,1,2,3]->[0,1,2,3,0,1] k =3

        left = 1

        if nums is None:
            return 0
            
        for right in range(1, len(nums)):
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left +=1
            
        return left
