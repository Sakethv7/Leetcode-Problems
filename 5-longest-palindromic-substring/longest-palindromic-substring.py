class Solution:
    def longestPalindrome(self, s: str) -> str:
        # fast and slow pointer, check if they are the same value, if not move, if you find them, we output from start to fast pointer's index's values
# only increment slow after you have found a similarvalue keep the this is brute force 2 for loops, check 

        res = ""
        reslen = 0

        for i in range(len(s)): 
        # Iterate through each character in the string as potential center
            #for all odd lengths
            left, right = i, i
            while left >=0 and right < len(s) and s[left]==s[right]: 
                # Expand outwards as long as left and right are within bounds and characters match
                if(right-left+1) > reslen: # If the current palindrome is longer than the previous one, update the result
                    res = s[left:right+1]
                    reslen = right - left + 1
                left -=1 # Move pointers outwards for the next comparison
                right +=1

            #even length
            left, right = i, i+1  # Set left and right pointers to adjacent positions, centered between i and i+1
            while left >=0 and right < len(s) and s[left]==s[right]:  # Expand outwards similarly as in the odd-length case
                if(right-left+1) > reslen:
                    res = s[left:right+1]
                    reslen = right - left + 1
                left -=1
                right +=1
        
        return res