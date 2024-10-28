class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        countchar = {}
        stack = []

        #countchar['i'] +=1
        
        for char in s:
            countchar[char] = countchar.get(char,0) + 1

        for i in range(len(s)): #need to return index
            if countchar[s[i]] == 1:
                return i
        
        return -1
            
        

                #return i when first unique character found

                   
