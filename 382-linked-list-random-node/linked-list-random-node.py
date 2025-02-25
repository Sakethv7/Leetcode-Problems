# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):       
        self.array = []
        while head: 
            self.array.append(head.val)
            head = head.next

    def getRandom(self):
        return random.choice(self.array)
        
        #     self.head = head

    # def getRandom(self) -> int:
    #     count = 0
    #     result = None
    #     current = self.head

    #     while current is not None:
    #         count += 1

    #         if random.randint(1, count) == 1:
    #             result = current.val 
    #         current = current.next
        
    #     return result

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()