# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1, leaves2 = [], []

        self.dfs(root1, leaves1)
        self.dfs(root2, leaves2)

        return leaves1 == leaves2

    def dfs(self, node: TreeNode, leaves: list):
        if not node:
            return

        if not node.left and not node.right:
            leaves.append(node.val)
        else:
            self.dfs(node.left, leaves)
            self.dfs(node.right, leaves)
        
