# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        #if node.left and node.right is None, cnt+=1

        if not root:
            return 0
        
        q = deque()
        q.append(root)
        depth = 1 #start depth at 1 for counting root node

        while q:
            size = len(q)

            for _ in range(size):
                node = q.popleft()
                
                if not node.left and not node.right: #if node has no left or right, that means it is a leaf node, we return the current value of depth
                    return depth

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            depth +=1 #we increment depth if we do not find it

        return depth
