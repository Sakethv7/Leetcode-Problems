# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            # Cycle detected
            if(fast == slow):
                break
        if fast is None or fast.next is None:
            return None

        #2nd part: r find the starting node of the cycle
        while head!=slow:
            head = head.next
            slow = slow.next
    

        return head

        