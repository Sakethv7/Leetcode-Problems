# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
# Initialize two pointers starting at the heads of both linked lists
        l1, l2 = headA, headB

        # Traverse both lists. When each pointer reaches the end of one list,
        # redirect it to the head of the other list.
        #
        # Why this works:
        # - If the two lists intersect, switching heads equalizes the total distance
        #   each pointer travels (A + B and B + A). They will eventually meet at
        #   the intersection node.
        #
        # - If the lists do NOT intersect, both pointers will eventually become None
        #   at the same time after traversing A + B length.
        while l1 != l2:
            # Move l1 to next node; if it reaches the end, jump to headB
            l1 = l1.next if l1 else headB

            # Move l2 to next node; if it reaches the end, jump to headA
            l2 = l2.next if l2 else headA

        # When they meet, either at the intersection node or both Null
        return l1