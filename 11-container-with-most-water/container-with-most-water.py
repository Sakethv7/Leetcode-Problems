class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxwater =0

        h = len(height)
        if h == 0:
            return 0
        
        if h == 1:
            return height[0]

# Area=min(height[left],height[right])×(right−left)   area = length * breadth, breadth is the distance between 2 pointers and length is the value of the pointer which is lesser than the other  basically it forms a rectangle

        left, right= 0, h-1

        while left< right:  
            area =  (right-left)*min(height[left], height[right]) # width or breadth * length
            maxwater = max(maxwater, area) 

            if height[left] < height[right]: 
                left+=1 #increment the pointer to move it forward and check other values
            elif height[left] > height[right]:
                right -=1 #decrement the pointer to go to other values
            else:
                right -=1

        return maxwater