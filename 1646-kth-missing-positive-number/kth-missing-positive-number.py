class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i, n = 0, len(arr)
        current, count_missing =  1, 0 # initialize first number

        while True:
            if i < n and arr[i] == current:
                i += 1
            else:
                count_missing += 1

            if count_missing == k:
                return current

            current += 1 #check next positive integer until you find on

        return -1 
