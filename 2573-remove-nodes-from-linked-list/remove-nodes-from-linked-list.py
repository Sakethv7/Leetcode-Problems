# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        stack = []
        while current_node is not None:
            while stack and stack[-1].val < current_node.val: #comparing stack's top element with the current value of linkedlist
                stack.pop() #pop the stack
            if stack: 
                stack[-1].next = current_node #top element points to currrent node
                
            stack.append(current_node) #push current node to stack
            current_node = current_node.next

        if stack:
            return stack[0] #returns bottom of the stack as head of the modified list
        else:
            return None
