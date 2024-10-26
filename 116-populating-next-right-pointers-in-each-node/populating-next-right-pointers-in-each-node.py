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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # O(1) solution
        # node = Node(0)
        if not root:
            return None

  # Initialize 'current' as the root node and 'next' as its left child (if exists)
        current, next = root, root.left if root else None

        while current and next:
            # Connect the left child's next to the right child
            current.left.next = current.right

            # If the current node has a next (i.e., not the last node in the current level),
            # connect the right child of the current node to the left child of the next node
            if current.next: 
                current.right.next = current.next.left
            
            # Move to the next node in the current level
            current = current.next
            if not current:
                current = next
                next = current.left

        return root