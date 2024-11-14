class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # find anarray answer answer[i] = abs(leftsum[i] - rightsum[i])

        answer = []
        leftsum = 0
        rightsum = sum(nums)
        a_sum = 0 # calculates abs(leftsum[i] - rightsum[i])

        for i in range(len(nums)):
            rightsum -= nums[i] #exclude current element in rightsum

            a_sum = abs(leftsum - rightsum)
            answer.append(a_sum)

            leftsum += nums[i]
        
        return answer