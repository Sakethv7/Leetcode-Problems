from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        windowstart = 0
        max_length = 0
        max_repeat_letter_count = 0
        freq = defaultdict(int)
        
        for windowend in range(len(s)):
            right_char = s[windowend]
            freq[right_char] +=1

            max_repeat_letter_count = max(max_repeat_letter_count, freq[right_char])

            if (windowend - windowstart +1 - max_repeat_letter_count)>k:
                left_char = s[windowstart]
                freq[left_char] -=1
                windowstart+=1

            max_length = max(max_length, windowend-windowstart +1)
        
        return max_length