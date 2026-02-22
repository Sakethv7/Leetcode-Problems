class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primeset = {2,3, 5, 7, 11, 13, 17, 19}
        result = 0

        for num in range(left, right+1):
            setbits = num.bit_count()
            if setbits in primeset:
                result += 1
        
        return result
    


            
            