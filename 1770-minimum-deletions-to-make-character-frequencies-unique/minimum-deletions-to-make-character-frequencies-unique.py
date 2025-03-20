class Solution:
    def minDeletions(self, s: str) -> int:
        deletions = 0
        count_freq = Counter(s) #map each character of the string and their frequency/value
        frequency = sorted(count_freq.values(), reverse = True) # sort in descending order
        n = len(frequency)

        for i in range(1, n): #Start with the second highest frequency (since the first one does not have a preceding frequency to compare with)
            if frequency[i] >= frequency[i-1]:
                desiredfrequency = max(0, frequency[i-1] - 1)  # Calculating the desired frequency
                deletions += frequency[i] - desiredfrequency # Calculating deletions needed
                frequency[i] = desiredfrequency # Updating the frequency of the ith element 
        
        return deletions