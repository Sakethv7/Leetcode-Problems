class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_d = 0   
        lastoccupied = -1
        n = len(seats)

        for i, seat in enumerate(seats):
            if seat == 1:
                if lastoccupied == -1:
                    max_d = i # no occupied seats before this, so distance is i
                else:
                    max_d =  max(max_d, (i-lastoccupied)//2)
                
                lastoccupied = i 
    
            
        max_d = max(max_d, n-1-lastoccupied)
        
        return max_d
