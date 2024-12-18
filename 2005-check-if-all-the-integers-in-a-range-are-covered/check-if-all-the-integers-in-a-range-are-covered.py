class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0] * 52

        for x in ranges:
            diff[x[0]] += 1
            diff[x[1] + 1] -= 1
        
        prefix = 0

        for i in range(1, right+1):
            prefix += diff[i]

            if i >=left and prefix == 0:
                return False
        
        return True