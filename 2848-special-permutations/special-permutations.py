class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        # permuations of nums is special if: 0 <= i< n-1 or nums[i] % nums[i+1] == 0 
        # nums[i+1] % nums[i] == 0

        MOD = 10**9 + 7
        n = len(nums)

        @lru_cache(None)
        def dp(mask, prev_idx):
            """ 
            mask: Bitmask representing selected numbers 
            prev_idx: Index of the last added number
            """
            if mask == (1 << n) - 1:  # All numbers used
                return 1
            
            count = 0
            for i in range(n):
                if not (mask & (1 << i)):  # If nums[i] is not used
                    if prev_idx == -1 or nums[prev_idx] % nums[i] == 0 or nums[i] % nums[prev_idx] == 0:
                        count += dp(mask | (1 << i), i)  # Mark nums[i] as used
                        count %= MOD
            
            return count

        return dp(0, -1)  # Start with an empty mask and no previous number