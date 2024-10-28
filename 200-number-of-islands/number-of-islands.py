class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # return number of islands, island = surrounded by water (0's) and is formed connecting adjacent lands (1's)horizontally or vertically. all four edges of the grid are all surrounded by water 0's
        #using recursion        
        def dfs(grid, i, j):
            #checking if i is greater or equal to no. of rows and j is greater than equal to number of columns
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != '1': 
                #checking if the cell is out of bounds or if its water <0 or 0
                return 0
            grid[i][j] = '0' # marking as visited

            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)
        
        island_count = 0
        for rows in range(len(grid)):
            for cols in range(len(grid[rows])):
                if grid[rows][cols] == '1':
                    island_count+=1
                    dfs(grid, rows, cols)
        
        return island_count