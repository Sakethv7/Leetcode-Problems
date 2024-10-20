class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        freq_count = {}
        max_count = 0
        windowstart = 0

        for windowend in range(len(fruits)):
            right_char = fruits[windowend]

            if right_char not in freq_count:
              freq_count[right_char] = 0
            freq_count[right_char] +=1

            while len(freq_count) >2: #can only fit 2
                left_char = fruits[windowstart]              
                freq_count[left_char] -= 1
                if freq_count[left_char]==0:

                    del freq_count[left_char]
                windowstart +=1
            
            max_count = max(max_count, windowend - windowstart+1) #count with the windo indices
        
        return max_count

