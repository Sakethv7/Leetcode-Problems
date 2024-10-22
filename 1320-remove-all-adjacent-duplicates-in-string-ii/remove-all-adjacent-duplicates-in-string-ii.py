class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] +=1 # adding the count of the character already in the stack when compared to character in the string which is the same. exqample ['a', 1] becomes ['a', 2] when char = a from the string 
            else:
                stack.append([char, 1])#appending the character and count in the stack in the same index
                #example: [b,1]
            
            if stack[-1][1] == k:
                stack.pop() #popping the character and its count which is stored at the same index as example: ['a',2]
        
        return ''.join( char*count for char, count in stack)