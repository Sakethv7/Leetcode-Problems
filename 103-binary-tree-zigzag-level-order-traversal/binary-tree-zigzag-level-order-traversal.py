# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            level=[]

            for i in range(level_size):
                currentNode = queue.popleft()
                level.append(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
                
            if len(result) % 2 ==1:
                level.reverse() # the odd numbered layers are reversed for zigzag
            result.append(level)
        return result