class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        prefix = min(strs, key = len) #shortest common prefix thing

        for i in range(len(prefix)):
            if not all (s.startswith(prefix[:i+1]) for s in strs):
                #retrurn the longest common prefix 
                return prefix[:i]
        
        return prefix