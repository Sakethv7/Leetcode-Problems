# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # return the head of the merged list, list1 and list2 merge
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                current = list1
                list1 = list1.next
            else:
                current.next =list2
                current = list2
                list2  = list2.next
            
        current.next = list1 if list1 else list2 # when either list1 or list2 is pointing at None after finishing the while loop, we point the current node's next to list1 if list1 is still there, else it would point to list2

        return dummy.next #head is stored at dummy.next