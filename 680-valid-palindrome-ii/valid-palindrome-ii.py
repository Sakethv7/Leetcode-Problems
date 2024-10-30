class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s, l, r): # Helper function to check if a substring is a palindrome
            while l<r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        
        left, right = 0, len(s)-1

        while left < right:

            if s[left] == s[right]:
                left +=1
                right -=1

            else:
                return isPalindrome(s, left+1, right) or isPalindrome(s, left, right-1) #we either remove character on l's poisition and see if it is a palindrome or check by removing character on right by decrementing (skipping either left or right value by +1 or -1 respectively)

        return True

