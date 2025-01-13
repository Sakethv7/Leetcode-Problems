class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = {}

        for num in hand:
            count[num] = 1 + count.get(num, 0)
        
        minheap = list(count.keys())    
        heapq.heapify(minheap) #orders the array into a heap with an order of minimum to mqsimum values

        while minheap:
            first = minheap[0]

            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minheap[0]:
                        return False
                    heapq.heappop(minheap)
                
        return True

