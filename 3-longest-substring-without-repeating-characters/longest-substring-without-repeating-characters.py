class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        mymap = {}# Dictionary to store the last index of each character
        max_length =0
        window_start = 0# Start of the current substring without repeats

        for window_end in range(len(s)):
            char = s[window_end]
             # If the character is in the map and within the current window, move the window start
            if char in mymap and mymap[char] >= window_start:
                window_start = mymap[char] + 1

        # Update the last index of the character
            mymap[char] = window_end
            
            max_length = max(max_length,window_end - window_start+1) # Calculate the max length of the substring

        return max_length
