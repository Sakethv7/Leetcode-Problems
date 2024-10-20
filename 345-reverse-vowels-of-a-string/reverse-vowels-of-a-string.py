class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s= list(s) #convert the string into list
        #ask interviewer if y is considered a vowel
        #reversing something generally means a 2 pointer method
        left,right =0, len(s)-1 #2 pointer method

        while(left<right):
            if(s[left] not in vowels):
                left+=1
            elif(s[right] not in vowels):
                right-=1
            else:
                s[left], s[right] = s[right], s[left]
                left+=1
                right-=1
        
        return "".join(s) #joining the string from list
