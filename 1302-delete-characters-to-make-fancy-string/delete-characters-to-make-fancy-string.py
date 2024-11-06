class Solution:
    def makeFancyString(self, s: str) -> str:
    
        result = [] 
        
        for char in s:
            # Check if the last two characters in result are the same as the current character
            if len(result) >= 2 and result[-1] == char and result[-2] == char:
                continue  # Skip adding the character if it creates three consecutive chars
            result.append(char)
        
        return ''.join(result) 