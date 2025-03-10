class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
            i = 0
            ans = 0
            count = 0
            n = len(nums)
            m = {}

            for j in range(n):
                # Increment the frequency of the current element
                m[nums[j]] = m.get(nums[j], 0) + 1
                # If the element's frequency is more than 1, increment the count of pairs
                if m[nums[j]] > 1:
                    count += m[nums[j]] - 1
                
                # While the count of pairs is at least k, adjust the window
                while i <= j and count >= k:
                    ans += n - j  # Add to answer the number of subarrays that can be formed from the current position
                    # Decrement the frequency of the element at the start of the window
                    m[nums[i]] -= 1
                    # If the frequency is still at least 1, decrement the count of pairs
                    if m[nums[i]] >= 1:
                        count -= m[nums[i]]
                    i += 1  # Move the start of the window
            
            return ans  # Return the total count of good subarrays
