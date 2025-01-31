class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        direct = [ [0,1], [0, -1], [1, 0], [-1, 0]]

        def invalid(r, c):
            return r<0 or c< 0 or r == N or c == N #to check if the grid is valid or not i.e. it is out of bounds
        visit = set()
        def dfs(r, c): #find the 1s in the grid
            if (invalid(r, c) or not grid[r][c] or (r, c) in visit):
                return
            visit.add((r, c))
            for dr, dc in direct:
                dfs(r + dr, c + dc)
        
        def bfs():
            res, q = 0, deque(visit)
            while q:
                length = len(q)
                for i in range(length):
                    r, c = q.popleft()
                    for dr, dc in direct:
                        currR, currC = r+dr, c + dc
                        if invalid(currR, currC) or (currR, currC) in visit:
                            continue
                        if grid[currR][currC]:
                            return res
                        q.append([currR, currC])
                        visit.add((currR, currC))
                res += 1
        
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r, c)
                    return bfs()
