class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #return true if ransome note can be constructed by using the letters from magazine and false otherwise 
        str_count = Counter(magazine)

        for char in ransomNote: 
            if str_count[char] == 0:  #Count the frequency of each character in 'magazine'
                return False
            # If the character is not found or its count is zero, 
            # it means magazine does not have enough of that character 
            # to build ransomNote, so return False
            else:
                str_count[char] -=1
                # If the character is available, decrease its count by 1 
                # that mean it has been usedd to build ransomNote
        
        return True


