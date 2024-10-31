class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []

        i, j = 0, 0

        while i< len(word1) and j< len(word2):
            res.append(word1[i]) # Add the character from word1 at index i to the result
            res.append(word2[j]) # Add the character from word1 at index j to the result
            i+=1
            j+=1
        res.append(word1[i:])  # Append any remaining characters from word1 (if it is longer than word2) even if there is no number character left.   Accesses elements from index i to the end of the array.
        res.append(word2[j:])   # Append any remaining characters from word2 (if it is longer than word1)
#Accesses elements from index j to the end of the array.
        return "".join(res)