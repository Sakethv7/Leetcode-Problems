class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #return the longest consecutive element's sequence. basically size of a subarray of consecutive elements

        num_set = set(nums)
        longest_sequence = 0
   #  Iterate over each number in the original list
        for num in nums:
        # Check if this number is the start of a sequence
         # If num - 1 is not in the set, num is the smallest in the current sequence
            if num - 1 not in num_set:
                next_num = num +1  # Initialize the next number in the sequence
                length = 1 # Start with a sequence length of 1 (current number itself)
                while next_num in num_set:
            #Keep increasing the length while consecutive numbers are found
                    length+=1 # Increase the sequence length
                    next_num +=1 # Move to the next consecutive number

                longest_sequence = max(longest_sequence, length)
        
        return longest_sequence

