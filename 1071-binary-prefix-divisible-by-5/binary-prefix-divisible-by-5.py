class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        curr = 0

        for n in nums:
            curr = (curr << 1) + n #shift curr one place behind, add n and then see if it is divisible by 5 or not
            res.append(curr % 5 == 0)
        
        return res