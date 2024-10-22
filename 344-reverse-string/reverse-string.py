class Solution:
    def reverseString(self, s: List[str]) -> None:
        stack = []

        # Push all characters onto the stack
        for c in s:
            stack.append(c)

        # Pop characters off the stack and place them back into the list
        for i in range(len(s)):
            s[i] = stack.pop()

        
        
