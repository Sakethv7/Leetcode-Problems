class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s)-1, 0

        while i>=0 and s[i] == " ": #start from the end of the string and check for spaces
            i -= 1 # Move to the left to skip spaces
        
        while i>=0 and s[i] != " ": # if no spaces that means there is a word
            length += 1
            i -=1
        
        return length #return length of the word

        #time O(n), space O(1)

