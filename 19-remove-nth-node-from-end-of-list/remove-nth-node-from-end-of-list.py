# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0, head) # create a dummy node to pointing to the head
        dummy = res # pointer to traverse the list 

        for _ in range(n):
            head = head.next # Move the head pointer n steps ahead
        
        while head:   # Traverse both 'head' and 'dummy' until 'head' reaches the end
            head = head.next
            dummy = dummy.next # after the loop finishes, dummy is at the node before nth node
        
        dummy.next = dummy.next.next # skip the nth node, thus removing it

        return res.next # points at the modified head of the linkedlist
    