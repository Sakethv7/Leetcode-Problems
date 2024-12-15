class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
    # Get the number of rows and columns
        m = len(grid)
        n = len(grid[0])

        # Iterate through the grid and check the conditions
        for i in range(m):
            for j in range(n):
                # Check condition 1: grid[i][j] == grid[i + 1][j] (if the cell below exists)
                if i < m - 1 and grid[i][j] != grid[i + 1][j]:
                    return False
                # Check condition 2: grid[i][j] != grid[i][j + 1] (if the cell to the right exists)
                if j < n - 1 and grid[i][j] == grid[i][j + 1]:
                    return False

        # If all conditions are satisfied, return True
        return True