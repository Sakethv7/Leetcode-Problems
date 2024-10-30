class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # #diff = target -n
        # prevMap ={}
        # n = len(numbers)

        # for i, num in enumerate(numbers):
        #     diff = target - num
        #     if diff in prevMap:
        #         return (prevMap[diff]+1, i+1)
        #     else:
        #         prevMap[num] = i
        
        # return _

        #for constant extra space, we can not use a hash map, so for this:
        n = len(numbers)
        start, end = 0, n-1

        while start <= end:
            if numbers[start] + numbers[end] == target:
                return [start+1, end+1]  # Return the 1-indexed positions of the numbers

            elif numbers[start] + numbers[end] < target:
                start +=1
            else: # numbers[start] + numbers[end] > target:
                end -=1
        
        return [] # Return an empty list if no solution is found