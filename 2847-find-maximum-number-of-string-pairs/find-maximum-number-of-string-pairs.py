class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        checkword = set()
        count  = 0
    
        for word in words:
            rev = word[::-1] #reverses the string 
            if rev in checkword:
                count += 1
            else:
                checkword.add(word)
        
        return count 