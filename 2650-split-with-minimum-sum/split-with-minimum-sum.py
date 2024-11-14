from queue import PriorityQueue 
class Solution:
    def splitNum(self, num: int) -> int:
        # num split it into num1 and num2, sum of the number of occurrences of each digit in num1 and num2 =  no. of occurences of num
        # return the min sum of num1 and num2
        num1, num2 = "", ""
        
        nums = [int(x) for x in str(num)]
        pq = PriorityQueue()
        
        for i in nums:
            pq.put(i)

        while not pq.empty():
            num1 += str(pq.get())
            if not pq.empty():
                num2 += str(pq.get())
        
        if num2:
            return int(num1) + int(num2)
        else:
            return int(num1)
