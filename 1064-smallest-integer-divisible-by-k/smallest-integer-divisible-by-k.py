class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        
        cur = 1
        res = 1
        prev = set() #constant set ups and look ups
        while cur % k:
            if cur in prev:
                return -1
            prev.add(cur)
            cur = 10*(cur%k) + 1
            res += 1
        
        return res