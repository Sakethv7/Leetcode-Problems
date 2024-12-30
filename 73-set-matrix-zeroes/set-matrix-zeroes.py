class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #solve it in place with O(1) memory
        
        rows, cols = len(matrix), len(matrix[0])
        rowzero = False  # To track if the first row needs to be zeroed

        # first iteration: Mark rows and columns to be zeroed
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0  # Mark the column
                
                    if r == 0:  # Mark the row (but skip the first row)
                        rowzero = True  
                    else:
                        matrix[r][0] = 0
                 
        
        # second iteration: Update the matrix based on markers
        for r in range(1, rows): # Start from the second row to preserve markers in the first row
            for c in range(1, cols):  # Start from the second column to preserve markers in the first column
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        # Handle the first column if matrix[0][0] is 0
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        
        if rowzero: # Handle the first row if rowzero is True
            for c in range(cols):
                matrix[0][c] = 0
    
