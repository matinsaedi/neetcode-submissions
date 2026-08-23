class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        row, col = len(grid), len(grid[0])
        queue = collections.deque([])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        fresh = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
    
        minutes = 0

        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (
                        0 <= nr < row and
                        0 <= nc < col and
                        grid[nr][nc] == 1
                        ):
                        grid[nr][nc] = 2 
                        queue.append((nr, nc))
                        fresh -= 1
            minutes += 1

        return minutes if fresh == 0 else -1