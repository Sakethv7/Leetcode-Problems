class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
            if stack and stack[-1] == char: #if top of the stack is equal to the character
                stack.pop() #pop the character
            else:
                stack.append(char) #append the character
        
        return ''.join(stack) #return the stack as a string with the appended characters