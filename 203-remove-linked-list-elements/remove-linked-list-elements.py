# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #node.val == val del node i.e. point to null/none
        
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current is not None and current.next is not None:

            if current.next.val == val:
                current.next = current.next.next # skip the next node and point to the one after it. thus removing it
            else:
                current = current.next
        
        return dummy.next 