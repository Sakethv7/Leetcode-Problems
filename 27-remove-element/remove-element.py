class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # return the first k elements which are not equal to val and also the number of non val elements
        # move all the occurences of this element to the end of the array, swap the last element with the val element in the array
        # we can keep appending the elements not in val into another array and count the number of elements in it and return it

        left = 0

        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right] #nums modified in-place
                left += 1 

        return left


