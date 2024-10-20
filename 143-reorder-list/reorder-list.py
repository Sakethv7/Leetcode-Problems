# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        
        slow, fast = head, head

        #find middle node
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next ##slow pointer is at the middle of the list now

        #slow is at the beg of the second half of the list, reverse the second part of the list
        second = slow.next
        slow.next = None # splitting first and second half of the linked list
        prev = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        #merge the lists
        #so we initialise pointers for the 2 half lists
        first = head
        second = prev
        while second:
            tmp1, tmp2 = first.next, second.next  #get the links and store them temporarily
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        



        