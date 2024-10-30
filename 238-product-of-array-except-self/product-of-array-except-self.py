class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)) # creatng an answer array which is of the size n of nums

        prefix = 1                           #initialising a prefix value 
        for i in range(len(nums)):          #from the start of nums iterate through, Iterate through nums from left to right
            res[i] = prefix                 # Assign the current prefix value to res[i]
            prefix = prefix * nums[i]       # Update the prefix by multiplying it with the current element
        
        postfix = 1                             #initializing a postfix value
        for j in range(len(nums)-1, -1, -1):    #loop starts from the end of nums, Iterate through nums from right to left
            res[j] = res[j]*postfix            #Multiply the current res[j] value with the postfix
            postfix = postfix * nums[j]        #Update the postfix by multiplying it with the current element
        
        return res



