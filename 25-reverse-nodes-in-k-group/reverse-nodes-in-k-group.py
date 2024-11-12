class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1 or head is None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy # Previous group's last node, is set to dummy

        while True:
            kth = prev_group # Check if there are at least k nodes left to reverse
            count = 0
            while kth is not None and count < k:
                kth = kth.next
                count += 1
                
            if kth is None:
                break  # Less than k nodes left, so we're done

            current = prev_group.next
            prev = None
            for i in range(k):
                temp = current.next
                current.next = prev
                prev = current
                current = temp
             # Connect with the previous part and the next part
            next_group = prev_group.next   # This is the first node of the reversed part
            prev_group.next = prev # Connect previous part to the new head of the reversed sublist
            next_group.next = current # Connect the end of the reversed sublist to the remaining list

            prev_group = next_group  # Move prev_group to the end of the reversed sublist
        return dummy.next


        