# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if number of nodes(p) = q and values of the nodes
        # p.vaue = q.value

        if not p and not q: #if both root nodes or trees are null
            return True

        if not p or not q or p.val != q.val: #if either of the root is null and the other is not null then it should return false and also if the root values are not equal then it should return false
            return False
        
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))  #returns the result of the DFS boolean operation which traverses the whole tree
