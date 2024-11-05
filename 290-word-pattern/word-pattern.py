class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        #pattern abba, string dog cat cat dog 
        # a maps to dog b maps to cat
        # Dictionary to store mappings from character to word and vice versa
        char_to_word = {}
        word_to_char = {}
        
        # Split the string into words
        words = s.split()
        
        # If the lengths don't match, the pattern doesn't fit
        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]
            
            # Check character to word mapping
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word
            
            # Check word to character mapping
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char

        return True



