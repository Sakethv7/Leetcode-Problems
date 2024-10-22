class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for i in path.split('/'):
            if stack and i == "..":
                stack.pop()  #pop elements if .. as it says to come out (pop) of the directory in the path
            elif i not in [".", "", ".."]:
                stack.append(i)
        
        return '/' + '/'.join(stack)