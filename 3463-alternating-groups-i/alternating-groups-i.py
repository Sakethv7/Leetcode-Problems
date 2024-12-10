class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        #return the number of alternating colors 

        count = 0
        n = len(colors)
        
        for i in range(len(colors)):
            if i== 0 and colors[i] != colors[n-1] and colors[i] != colors[i+1]:
                count += 1
            elif i == n-1 and colors[i] != colors[0] and colors[i] != colors[i-1]:
                count += 1
            elif i != 0 and i != n-1 and colors[i] != colors[i-1] and colors[i] != colors[i+1]:
                count += 1

        return count 