class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {} #hashmap, key = index (starting value) value = [length of LIS, count]
        lenLIS, res = 0, 0 # length of longest increasing subsequence, count of LIS

        for i in range(len(nums)-1, -1, -1): #iterating through array from reverse order
            maxlen, maxcnt = 1, 1 #len, count of LIS that starts from i

            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]: #check if in increasing order
                    length, count = dp[j] # len, cnt of LIS starting from j
                    if length + 1 > maxlen:
                        maxlen, maxcnt = length + 1, count
                    elif length + 1 == maxlen:
                        maxcnt += count

            if  maxlen > lenLIS: # Update the global maximum length of LIS (lenLIS) and its count (res)
                lenLIS, res = maxlen, maxcnt
            elif maxlen == lenLIS:
                res += maxcnt  # Found another LIS of the same length, increment the total count

            dp[i] =  [maxlen, maxcnt]  # Store the length and count of LIS starting from index i in the dp dictionary

        return res  # Return the total number of LIS with the maximum length