"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        current = head
        old_new = {}# Dictionary to map original nodes to their copies 

        # First pass: create new nodes and store them in the dictionary
        while current:
            node = Node(x=current.val)  # Create a new node with the same value
            old_new[current] = node  # Map original node to the new node
            current = current.next  # Move to the next node
        
        current = head
  # Second pass: set the next and random pointers for copied nodes
        while current:
            new_node = old_new[current]  # Get the copied node
            # Set the next pointer of the copied node
            new_node.next = old_new[current.next] if current.next else None
            # Set the random pointer of the copied node
            new_node.random = old_new[current.random] if current.random else None
            current = current.next  # Move to the next node
        
        return old_new[head]
