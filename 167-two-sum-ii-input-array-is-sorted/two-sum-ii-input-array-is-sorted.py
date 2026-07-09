class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        first, last = 0, len(numbers)-1
        s = 0
        result = []

        while first < last:
            s = numbers[first] + numbers[last]
            if s > target:
                last -= 1
            elif s < target:
                first += 1
            else: #sum == target
                return [first+1, last+1]
 
        return []