class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # sentence only isalpha
        #circular when: last character of word = first character of next word 
        # and last character of last word in sentence = first character of first word in sentence
      
        words = sentence.split() #splits the sentence into words and takes care of the spaces
        
        # The last character of the last word should match the first character of the first word
        if words[0][0] != words[-1][-1]:
            return False
        
        # Check each pair of consecutive words to ensure circularity
        for i in range(1, len(words)):
            # If the last character of the previous word does not match the first character of the current word
            if words[i - 1][-1] != words[i][0]:
                return False
        
        # If all checks pass, the sentence is circular
        return True