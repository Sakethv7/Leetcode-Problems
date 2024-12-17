class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [0] * 101

        for birth, deaths in logs:
            years[birth-1950] += 1 # Mark birth year as +1
            years[deaths-1950] -= 1 # Mark death year as -1
        
        max_pop, current_pop, max_year = 0, 0, 0

        for i in range(101):
            current_pop += years[i] # Update the population using prefix sum
            if current_pop > max_pop:
                max_pop = current_pop
                max_year = 1950 + i # Convert back to actual year
        
        return max_year