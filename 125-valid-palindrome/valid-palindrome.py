class Solution:
    def isPalindrome(self, s: str) -> bool:
        #if a character is not alpha or numerical, increment left pointer and decrement right pointer
        # if left character == right character ( need to be lowercase as well)

        left = 0
        right = len(s)-1
  
        while left<right:
            if not s[left].isalnum():  # Move the left pointer until we find an alphanumeric character
                left +=1

            elif not s[right].isalnum(): # Move the right pointer until we find an alphanumeric character
                right -=1
            
            elif s[left].lower() != s[right].lower(): # Compare characters
                return False
            else:     # Move pointers inward only if characters match
                left +=1  
                right -=1
        
        return True
