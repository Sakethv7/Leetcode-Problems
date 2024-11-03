class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # str1, str2 return the index of first occurence of needle in haystack or -1 if needle not in haystack

        for i in range(len(haystack)+1 - len(needle)):
            if haystack[i : i+len(needle)] == needle:
                return i
            
        return -1        
           
            # for j in range(len(needle)):
            #     if haystack[i+j] != needle[j]:
            #         break
            #     if haystack[i+j] == needle[j]:
            #         return i

       