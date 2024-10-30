# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       
# Step 1: Initialize a dummy node to form the result linked list
        dummy = ListNode()
        curr = dummy
        carry = 0 #will store the carry-over value during addition

    #step 2:Iterate while there are nodes in l1, l2, or a carry to add
        while l1 or l2 or carry:
        # Get the value of the current nodes; if the node is None, use 0
            v1 = l1.val if l1 else 0
            v2 =  l2.val if l2 else 0

            #new digit
            # Step 3: Calculate the sum of values and carry
            val = v1+v2+carry
            carry  = val // 10 # Update the carry for the next iteration
            val = val % 10 # Store the last digit of the current sum in the new node
            curr.next = ListNode(val)  # Add the new digit to the result list

        # Move to the next node in the result list
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next # Step 4: Return the next of dummy node (head of the result list)
            