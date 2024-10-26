# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        if not root:
            return []
            
        def dfs(node, current_path):
            if not node:
                return []

            current_path += str(node.val) #add the value as a string into current path which is passed as a string

            if not node.left and not node.right:
               result.append(current_path) 

            else:
                dfs(node.left, current_path + "->")
                dfs(node.right, current_path + "->")       #concatenate array with current path to give output      
            
        dfs(root, "") #pass root and an empty string as an argument

        return result
            

        