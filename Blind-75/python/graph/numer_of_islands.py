from collections import deque
class Solution():
    def number_of_islands(self, grid):
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0
        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    self.bfs(i, j, grid, visited)
                    count += 1
        return count
    
    def bfs(self, r, c, grid, visited):
        rows, cols = len(grid), len(grid[0])
        visited.add((r,c))
        q = deque([(r,c)])
        while q:
            cr, cc = q.popleft()
            for dr, dc in [(0,1), (0,-1), (1,0), (-1, 0)]:
                nr, nc = cr + dr, dc + cc
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited and grid[nr][nc] == 1:
                        visited.add((nr,nc))
                        q.append((nr,nc))   

if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 1, 1], [0, 1, 0], [0, 0, 1]]
    print(sol.number_of_islands(grid))