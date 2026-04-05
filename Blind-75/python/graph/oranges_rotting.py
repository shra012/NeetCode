from collections import deque
class Solution():
    def oranges_rotting(self, grid):
        if not grid:
            return 0
        q = deque()
        fresh = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        time = 0
        while q and fresh > 0:
            time += 1
            for _ in range(len(q)):
                cr, cc = q.popleft()
                for dr, dc in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = dr + cr, dc + cc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
        return time if fresh == 0 else -1


if __name__ == "__main__":
    sol = Solution()
    grid = [
    [2,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,2],
]
    print(sol.oranges_rotting(grid))