class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height)-1
        water_trap = 0
        leftmax, rightmax =  height[l], height[r]

        while l < r:
            if leftmax < rightmax:
                l += 1
                leftmax = max(leftmax, height[l])
                water_trap += leftmax - height[l]
    
            else:
                r -= 1
                rightmax = max(rightmax, height[r])
                water_trap += rightmax - height[r]
                
        return water_trap