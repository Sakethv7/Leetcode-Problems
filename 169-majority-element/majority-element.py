class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #majority element- appears more than n/2 times 

        count = Counter(nums)
        n = len(nums)

        for num, freq in count.items():
            if freq > n//2:
                return num
    
                

