class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for p in path.split('/'):
            if stack and p == "..":
                stack.pop()  #pop elements if .. is the component while splitting
            elif p not in [".", "", ".."]:
                stack.append(p)
        
        return '/' + '/'.join(stack)