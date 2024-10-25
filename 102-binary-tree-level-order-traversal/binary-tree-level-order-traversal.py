# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#returning level order traversal means returning the array of nodes

from queue import Queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return [] #return empty list if root node is Null/None

        queue = Queue()
        queue.put(root)

        result =[]

        while not queue.empty():
            level_size = queue.qsize()
            level =[]  #initilize a level list

            for _ in range (level_size):
                currentNode = queue.get()
                level.append(currentNode.val)

                if currentNode.left:
                    queue.put(currentNode.left)
                if currentNode.right:
                    queue.put(currentNode.right)
                    
            result.append(level)
        
        return result
