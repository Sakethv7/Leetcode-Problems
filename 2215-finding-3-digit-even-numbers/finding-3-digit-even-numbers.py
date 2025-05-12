from collections import Counter
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = Counter(digits)
        result = []

        for num in range(100, 1000, 2): # loop through all even 3 digit numbers
            parts = [num//100, (num//10) % 10, num % 10]
            count = Counter(parts)
            if all(freq[d] >= count[d] for d in count):
                result.append(num)
        
        return result
