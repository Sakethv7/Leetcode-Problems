class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        char_count = {}

        for word in words:
            for c in word:
                char_count[c] = char_count.get(c, 0) + 1
        
        num_words = len(words)

        for count in char_count.values(): #count takes the value of the values of keys in char_count map/dictionary
            if count % num_words != 0:
                return False
        
        return True