# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = TreeNode(0) # dummy node to keep track of new root
        self.lastnode = dummy # pointer to consutrcut new tree

        def inorder(node):
            if not node:
                return 
            
            inorder(node.left) # visit left subtree

            node.left = None # remove left child
            self.lastnode.right= node #attach to the right
            self.lastnode = node # prepare node for next inorder traversal

            inorder(node.right) # visit right subtree
        
        inorder(root)
        return dummy.right # return the new root