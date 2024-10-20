class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set()
        for char in sentence:
            current_char= char.lower()
            if current_char.isalpha():
                seen.add(current_char)

        return len(seen) ==26
            
        

    
        