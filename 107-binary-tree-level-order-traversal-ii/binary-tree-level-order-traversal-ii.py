# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result =[]
        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue) #take length of queue
            level = [] #initialize the level list

            for _ in range(level_size): #traverse through the queue/level
                currentNode = queue.popleft()
                level.append(currentNode.val)

                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
                           
            result.append(level)
        return result[::-1]  #reverse the list