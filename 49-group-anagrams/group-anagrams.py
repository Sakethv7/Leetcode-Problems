class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #initilise an empty hashmap, iterate through the string using enumerate 
        anagrams = defaultdict(list)

        # Iterate through each string in the input list
        for s in strs: #for strings in the list strs
            count = [0]*26 #initilisean array with 26 (siginifiying 26 letters)

            # Count the frequency of each character in the string
            for char in s: 
                count[ord(char) - ord('a')] +=1
            
            key = tuple(count)
            anagrams[key].append(s)
        
        return list(anagrams.values())





