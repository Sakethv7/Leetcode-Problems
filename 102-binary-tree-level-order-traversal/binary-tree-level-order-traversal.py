# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return [] #return empty list if root node is Null/None

        queue = deque()
        queue.append(root)

        result =[]

        while queue:
            level_size = len(queue)
            level =[]  #initilize a level list

            for _ in range (level_size):
                currentNode = queue.popleft()  #gets the front element of queue
                level.append(currentNode.val)

                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
                    
            result.append(level)
        
        return result