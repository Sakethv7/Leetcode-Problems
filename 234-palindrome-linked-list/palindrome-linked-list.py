# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        #find middle which is slow
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        
        #reverse the list now
        prev = None # create a pointer and point it to null
        while slow is not None:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp 

        #check for palindrome by comparing the starting nodes of the list and the reversed list
        l,r = head, prev
        while r:
            if l.val != r.val: #compare values on that pointer
                return False
            l = l.next
            r = r.next
        return True
