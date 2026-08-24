class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        q = collections.deque([])
        row, col = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    q.append((i, j))

        level = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < row and
                       0 <= nc < col and
                       grid[nr][nc] == 2147483647):
                       grid[nr][nc] = level
                       q.append((nr, nc))
            level += 1