class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        subset_size = n // k
        
        # Check if it's possible to divide nums into k subsets
        if any(v > k for v in Counter(nums).values()):
            return -1

        # Precompute valid subsets and their incompatibilities
        subsets = {}
        for subset in range(1 << n):  # Iterate over all possible subsets
            if bin(subset).count('1') == subset_size:  # Ensure correct size
                elements = [nums[i] for i in range(n) if subset & (1 << i)]
                if len(elements) == len(set(elements)):  # Ensure no duplicates
                    subsets[subset] = max(elements) - min(elements)

        # DP array to store minimum incompatibility
        dp = {0: 0}  # Start with no elements used
        
        for mask in range(1 << n):  # Iterate over all states
            if mask not in dp:
                continue
            used_count = bin(mask).count('1')
            if used_count % subset_size == 0:  # Start a new subset
                for subset, incompatibility in subsets.items():
                    if mask & subset == 0:  # Ensure no overlap
                        dp[mask | subset] = min(dp.get(mask | subset, float('inf')), dp[mask] + incompatibility)

        return dp.get((1 << n) - 1, -1)



