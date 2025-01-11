class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        max_freq =  max(freq.values()) # finds the maximum frequency of any element in the input array
        buckets = [[] for _ in range(max_freq + 1)]  # Create buckets from 0 to max_freq

        for num, count in freq.items(): # grouping num and count together grouped on the basis of their respective counts
            buckets[count].append(num) 
            #freq = Counter([1, 1, 1, 2, 2, 3])
            # freq = {1: 3, 2: 2, 3: 1}
        
        res = []
        for i in range(max_freq, 0, -1): # Traverse buckets from high to low frequency because buckets become ordered in ascending so we get the largest frequencies at the end. 

        #max_freq = len(buckets) - 1
            for num in buckets[i]: 
                res.append(num)
                if len(res) == k:
                    return res
        


