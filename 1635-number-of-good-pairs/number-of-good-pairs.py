class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # # good pair is when (i,j ) where num[i] ==num[j] , indexes matter here
        # # initialize a count for good pairs
        # count =0
        # # 2 pointer solution with 2 for loops
        
        # # loops for all possible pairs, where j>i
        # for i in range( len(nums)):
        #     for j in range( i+1, len(nums)):

        #         if(nums[i]== nums[j]):
        #             count +=1

        # return count

        count = 0
        freq = defaultdict(int)  
        #This creates an empty defaultdict named freq. The default value for any new key is set to 0 (because we are using int, which defaults to zero).

        for num in (nums): #iterate through the list nums via num
            count = count+ freq[num]  # add the occurence of the number in count
            freq[num] = freq[num] + 1 #update the frequency
        
        return count