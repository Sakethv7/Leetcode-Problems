class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(string):
            
            stack = []
            for char in string:
                if char!='#':
                    stack.append(char)
                elif stack:
                    stack.pop()

            return ''.join(stack)

        return process(s) == process(t)


        #used divide and conquer rule using helper function and used stack data structure to append and pop
                