class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        n = columnNumber
        result = ""

        while n>0:

            result = chr(ord('A') + (n-1)%26) + result
            n = (n-1) // 26
        
        return result

