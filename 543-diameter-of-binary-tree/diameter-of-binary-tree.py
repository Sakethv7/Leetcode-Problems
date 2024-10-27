# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = [0] #make it a list as integer is immutable, list can be mutated
        
        def diameter(node):
            if not node:
                return 0
            
            leftlength = diameter(node.left) #recursion to traverse the tree for left or right nodes to check diameter
            rightlength = diameter(node.right)
            
            # Update the diameter if the path through this node is longer
            max_diameter[0] = max(max_diameter[0], leftlength + rightlength)
            
            return max(leftlength, rightlength) + 1    # Returning the depth of the subtree at current node

        diameter(root) #start the recursion

        return max_diameter[0]