class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        coordinates = set()

        for start, end in nums:
            for point in range(start, end + 1):
                coordinates.add(point)
        
        return len(coordinates)