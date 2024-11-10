class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # res = [1] # Initialize the first row of Pascal's triangle

        # for i in range(rowIndex):  # Generate rows up to the specified rowIndex
        #     next_row = [0]*(len(res)+1)   # Create a new row with an additional element, initialized to 0

        #     for j in range(len(res)): # Populate next_row by adding elements from the previous row
        #         next_row[j] += res[j]
        #         next_row[j+1] += res[j]
            
        #     res = next_row  # Update res to the new row

        # return res
        

        # optimized version using O(rowIndex) extra space

        res = [1] * (rowIndex+1)

        for i in range(1, rowIndex+1):
            for j in range(i-1, 0, -1):    # Update from the end to the beginning to avoid overwriting needed values
                res[j] += res[j-1]
        
        return res