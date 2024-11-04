class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0]) # Sort intervals by their start time to facilitate merging
        output= [intervals[0]] # Initialize output with the first interval

        for start, end in intervals[1:]: # Iterate through remaining intervals
            lastend = output[-1][1]  # Get the end of the last interval in output
# Get the end of the last interval in output
            if start<= lastend: 
                # If current interval overlaps with the last interval in output, merge them
                output[-1][1] = max(lastend, end)  # Update the end of the last interval to the max end value
            else:
                output.append([start, end]) # No overlap, add the current interval as a new interval
            
        return output