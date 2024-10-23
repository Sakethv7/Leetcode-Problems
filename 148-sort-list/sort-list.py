# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #using recursion and merge sort #nlogn time and o(n) space
        #divide the list until each node is seperate eg 4-2-3-1 becomes 4-2 and 3-1 and then 4, 2, 3, 1
        if not head or not head.next:
            return head
        left = head
        right = self.getMid(head)  #helper function to get mid value (right is the middle pointer)
        tmp = right.next #save right.next in temp  
        right.next = None # Break the list into two halves
        right = tmp

        left = self.sortList(left) #recursion
        right = self.sortList(right) #recursion
        return self.merge(left, right) #merge the sorted halves

    def getMid(self, head):
        slow, fast = head, head.next 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next  
        return slow
    
    def merge(self, list1, list2):
        tail = dummy = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next