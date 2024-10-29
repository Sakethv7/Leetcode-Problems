class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #return indices of the 2 numbers such that they addup to target     

        prevMap = {} # tracks the elements in the array once we have iterated through them. via index, value

        for i, n in enumerate(nums): #enumerate because we need index and value from the nums, so we convert it into a set 
            diff = target-n #with diff we can compare if there is an element which can sum with the current n for target
            if diff in prevMap:
                return(prevMap[diff], i) #return the indices
            else:
                prevMap[n] = i
        return _ #returning nothing as method is integer type we need to have a return statement at the end
