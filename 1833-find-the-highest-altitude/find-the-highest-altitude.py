class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # n+1 points at different altitudes 
        # gain array where gain[i] is the net gain in altitude between points i and i+1
        # return the highest altitude of a point
        # steps down is -ve, steps up is +ve
        #The values in gain[] don’t tell you directly where you are but how much the altitude changes with each step
        
        altitude = 0
        max_altitude = 0

        for change in gain:
            altitude += change
            max_altitude = max(max_altitude, altitude)
        
        return max_altitude