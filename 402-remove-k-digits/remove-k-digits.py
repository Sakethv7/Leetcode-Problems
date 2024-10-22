class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack =[] # holds the digits of the smallest numbers
 
        for n in num:
            while stack and k>0 and stack[-1] > n: #top of the stack is greater than n
                stack.pop() #remove the digit
                k-=1 #decrement k as we removed one digit
            stack.append(n) #add the current digit to the stack
        
        #if there are digits to be removed, we can use this while loop to remove from the end of the stack
        while k>0:
            stack.pop()
            k-=1
        
        result = ''.join(stack).lstrip('0')  #strip leading zeroes and join the stack into a string to form result
        return result if result else '0' #return result or 0 if the result is an empty string