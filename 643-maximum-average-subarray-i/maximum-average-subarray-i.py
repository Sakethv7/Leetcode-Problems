class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowstart, windowsum = 0, 0.0
        max_average= float(-inf)

        #windowend iterates through the array till the window ends at k-1 from start
        for windowend in range(len(nums)): #iterates till k this loop using an if statement below
            windowsum += nums[windowend]  #add the new element to sum

            if(windowend>= k-1):
                max_average = max(max_average, windowsum/k) #will store the max average every time the loop iterates
                #slide the window forward
                windowsum-= nums[windowstart] #moving the window forward by replacing it with the next index
                windowstart +=1

        return max_average
