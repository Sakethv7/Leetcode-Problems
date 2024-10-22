from collections import Counter
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        hashmap = {}

        count = Counter(nums)

        for num, count in count.items():
            if count ==1:
                return num
