"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        q = deque([root])

        while q:
            size = len(q)
            prev = None
            
            for _ in range(size):
                node = q.popleft()
                
                # Connect the 'next' pointer
                if prev:
                    prev.next = node
                prev = node

                # Add children to the queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # Set the 'next' of the last node at the level to None
            if prev:
                prev.next = None
        
        return root