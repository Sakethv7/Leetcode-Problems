class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastindex = {}

        for index, char  in enumerate(s):
            lastindex[char] = index

        res = []
        size, end = 0, 0

        for i, char in enumerate(s):
            size += 1
            end = max(end, lastindex[char])

            if i == end:
                res.append(size)
                size = 0
        
        return res