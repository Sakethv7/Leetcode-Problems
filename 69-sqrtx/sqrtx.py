class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        
        left, right = 1, x

        res = 0
        
        while(left<=right):
            mid  = left + ((right-left)//2) # calculating the half way to compare with x
            if(mid**2 > x): # if m^2 is greater than x
                right = mid-1 # we decrement right pointer to search more left
            elif(mid**2 < x):
                left = mid+1 # here we increment left pointer to search more towards right
                res = mid # here mid value could be the result as we need to round to nearest integer. like suppose 8 is the number, 2.8.. is square rooot, m becomes 2 here and the result is also 2
            else:
                return mid # cases when mid**2 == x
        return res