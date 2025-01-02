class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize the first row with all 1s
        # This represents the number of ways to reach each cell in the last row of a grid.
        # Since there's only one way to traverse rightmost or bottom-most paths in a grid (straight line),
        # all elements in the row are initialized to 1
        row = [1] * n

        # Loop through the rows of the grid from bottom to top (excluding the bottom row already initialized).
        # The idea is to calculate the number of unique paths to reach each cell in the current row
        # using the previously initialised row

        for i in range(m - 1):
            newRow = [1] * n 
            # Create a new row, also initialized with all 1s
            # Each new row will be updated based on the current row's values

            for j in range(n-2, -1, -1):
                # The value at newRow[j] is the sum of:
                #   1. The value to the right in the same row (newRow[j+1])
                #   2. The value directly below it in the previous row (row[j])
                newRow[j] = newRow[j+1] + row[j]
           # Update the current row to the newly computed row.
            # This effectively moves up one row in the grid.     
            row = newRow
# After processing all rows, the top-left cell's value will be stored in row[0],
        # which is the total number of unique paths from the top-left corner to the bottom-right corner.
        return row[0]