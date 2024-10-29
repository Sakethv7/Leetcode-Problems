class Solution:
    def longestPalindrome(self, s: str) -> int:
        #string s, initiliase a hashmap, populate it

        stringcount = Counter(s)
 # Count the frequency of each character in the string
        palindrome_length = 0
        oddfound = False

        # Iterate through the frequencies
        for  value in stringcount.values():
            if value%2 ==0:
                palindrome_length += value
            else:
                palindrome_length += value-1
                oddfound = True
            
            # Add the central character if any odd frequency was found
        if oddfound == True:
            palindrome_length +=1
        
        return  palindrome_length

'''
        Example Run for "abccccdd"
Frequency Map: {'a': 1, 'b': 1, 'c': 4, 'd': 2}
For 'a' and 'b', they are odd, so palindrome_length += 0 and oddfound = True.
For 'c', it’s even, so palindrome_length += 4.
For 'd', it’s even, so palindrome_length += 2.
After the loop, since oddfound = True, we add 1 to palindrome_length.
Final Output: 7 (correct answer)

'''