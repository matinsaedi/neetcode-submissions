class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(i, j):
            q = collections.deque([(i, j)])
            visited.add((i, j))

            while q:
                r, c = q.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (nr in range(row) and
                       nc in range(col) and
                       grid[nr][nc] == "1" and
                       (nr, nc) not in visited):
                       q.append((nr, nc))
                       visited.add((nr, nc))

        row, col = len(grid), len(grid[0])
        visited = set()
        islands = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1
        return islands
