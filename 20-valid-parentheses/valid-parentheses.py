class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ['{', '(', '[']:
                stack.append(char)
            else:
                if not stack:    # If stack is empty, it means there's no matching opening bracket
                    return False
            
                top = stack.pop()  # Pop the top of the stack to check against the closing bracket
   
   # Check if the popped element matches the current closing bracket
                if char =='}' and top!='{':
                    return False
                    
                if char ==')' and top!='(':
                    return False
                
                if char ==']' and top!='[':
                    return False

        return True if not stack else False