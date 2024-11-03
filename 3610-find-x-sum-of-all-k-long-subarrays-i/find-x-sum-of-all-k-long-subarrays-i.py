class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        answer = []  # of lenth n-k+1
        #answer[i] is the x-sum of the subarray nums[i,.... i + k-1]
      # Stores x-sums of each k-length subarray
        n = len(nums)
        
        # Traverse through each k-length subarray
        for i in range(n - k + 1):
            subarray = nums[i:i + k]  # Get k-length subarray
            freq = Counter(subarray)  # Count frequencies of elements
            
            # Get top x elements by frequency, and in case of tie, by element value
            top_x_elements = nlargest(x, freq.items(), key=lambda item: (item[1], item[0]))
            
            # Calculate the sum of the top x elements
            x_sum = sum(value * count for value, count in top_x_elements)
            answer.append(x_sum)
        
        return answer