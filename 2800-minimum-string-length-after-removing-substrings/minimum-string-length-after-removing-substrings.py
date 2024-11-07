class Solution:
    def minLength(self, s: str) -> int:
        stack = []  # Use a stack to keep track of characters
        
        for char in s:
            # Check if adding the current character forms "AB" or "CD" with the top of the stack
            if stack and ((stack[-1] == 'A' and char == 'B') or (stack[-1] == 'C' and char == 'D')):
                stack.pop()  # Remove the last character if it forms "AB" or "CD"
            else:
                stack.append(char)  # Otherwise, add the character to the stack
        
        # The length of the stack is the minimum possible length of the string after all removals
        return len(stack)