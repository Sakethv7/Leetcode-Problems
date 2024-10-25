# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        res = []
        q = deque()
        q.append(root)
        level_avg = 0

        while q:
            level_sum = 0  #initilize size, sum of levels here
            size = len(q)
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val  #add the value of the nodes in level_sum

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            level_avg = level_sum/size  #take level_avg
            res.append(level_avg)  # for each loop run, level_avg is appended to the result list
         
        return res


