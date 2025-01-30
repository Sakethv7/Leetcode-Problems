# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = defaultdict(list) #dictionary/hashmap
        res = []

        def dfs(node):
            if not node:
                return "null"
            
            traversed_string = ",".join([str(node.val), dfs(node.left), dfs(node.right)]) #recursion to traverse the left node and the right node and store the current node 

     #append the node already there if its not a duplicate to the hashmap/dictionary
            subtrees[traversed_string].append(node)

            if len(subtrees[traversed_string]) == 2:
                res.append(node) #if it had already been visited that means it is a duplicate so append it to the result
    
            return traversed_string #return the serialized subtreee
        
        dfs(root) #call the dfs function
        return res
