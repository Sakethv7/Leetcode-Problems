class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed) # Initialize a set with allowed characters for faster lookup
        res = len(words) # Start with all words being potentially consistent
                
        for word in words:  # Check each word in the list of words
            for char in word:
                # If any character in the word is not in the allowed set, reduce res and break
                if char not in allowed_set:
                    res -= 1
                    break

        return res