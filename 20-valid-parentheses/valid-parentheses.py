class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        for character in s:
            if character in ['(', '[', '{']:
                stack.append(character)
            else:
                if not stack: #check if the stack is empty, so that we do not pop if its empty, causing stack underflow
                   return False

                top = stack.pop()

                if character == ')' and top !='(':
                    return False
                if character == '}' and top!='{':
                    return False
                if character ==']' and top!='[':
                    return False
        
        return not stack #if the brackets were all matching then stack becomes empty after being poppped out. 
