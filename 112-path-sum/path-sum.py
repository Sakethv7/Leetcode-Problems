# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right:
            return targetSum == root.val #if there is no left or right node then we will return a boolean value that compares targetSum with the value at root node

        leftsum = self.hasPathSum(root.left, targetSum-root.val) #recursive function passing left node and targetsum-root.val, subtracts the value of the current left node 
        rightsum = self.hasPathSum(root.right, targetSum-root.val) #same here with the right

        return leftsum or rightsum #combined results, if either left side or right side path is equal to targetsum it will return true else false

    
        
        



    