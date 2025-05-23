class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        #shit = moving the leftmost character of s to the rightmost position
        #first character (leftmost) 0, shifted to rightmost position, end n-1

        if len(s) != len(goal):
            return False
        
        # #By concatenating s with itself (i.e., s + s), all possible rotations of s are contained within this new string.
        # rotated_s = s+s

        # return goal in (rotated_s)

        for _ in range(len(s)):
            if s == goal:
                return True
            s =s[1:] + s[0]  # Rotate `s` by moving the first character to the end
        
        return False