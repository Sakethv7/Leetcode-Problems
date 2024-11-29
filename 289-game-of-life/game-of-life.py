class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        def countNeighbors(r: int, c: int) -> int:
            """
            Counts the number of live neighbors for a cell at position (r, c).

            Args:
                r: Row index of the cell.
                c: Column index of the cell.

            Returns:
                The number of live neighbors.
            """
            
            neighbors = 0
            # Iterate over the 8 possible neighbors
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if (i == r and j == c) or i < 0 or j < 0 or i >= ROWS or j >= COLS:
                        # Skip the cell itself or out-of-bounds indices
                        continue
                    # Count live cells (1 or 3 because 3 indicates a live cell in transition)
                    if board[i][j] in [1, 3]:
                        neighbors += 1
            return neighbors

        # First pass: Determine the next state for each cell
        ROWS, COLS = len(board), len(board[0])  # Dimensions of the grid
        for r in range(ROWS):
            for c in range(COLS):
                live_neighbors = countNeighbors(r, c)
                if board[r][c] == 1:  # Current cell is alive
                    if live_neighbors in [2, 3]:
                        # Cell remains alive
                        board[r][c] = 3  # 3 means "alive in the next state"
                    else:
                        # Cell dies
                        board[r][c] = 1  # 1 means "was alive but will die"
                elif board[r][c] == 0:  # Current cell is dead
                    if live_neighbors == 3:
                        # Cell becomes alive
                        board[r][c] = 2  # 2 means "dead but will become alive"

        # Second pass: Update the board to the final state
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 1:  # Cell was alive but is now dead
                    board[r][c] = 0
                elif board[r][c] in [2, 3]:  # Cell becomes or remains alive
                    board[r][c] = 1