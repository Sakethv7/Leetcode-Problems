class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #heap solution- max heap
        
        maxHeap = [-int(n) for n in nums]
        heapq.heapify(maxHeap) #sorts the heap in ascending

        while k > 1:
            heapq.heappop(maxHeap) #pops 0th element. python only has minheap so when we made maxheap negative, the min heap worked like maxheap for us, removing the lowest negative value at 0th point
            k -= 1
        
        #After one pop, k becomes 1, and the loop stops.


        return (-maxHeap[0]) #return the 0th element after the original 0th element was popped. and we return by -ve sign which makes the heap element poisitive.