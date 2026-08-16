class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(i, j):
            q = collections.deque([(i, j)])
            visited.add((i, j))

            while q:
                r, c = q.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    i, j = r + dr, c + dc

                    if (i in range(row) and
                       j in range(col) and
                       grid[i][j] == "1" and
                       (i, j) not in visited):
                       q.append((i, j))
                       visited.add((i, j))

        row, col = len(grid), len(grid[0])
        visited = set()
        islands = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1
        return islands
