class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def bfs(i, j):
            count = 0
            queue = collections.deque([(i, j)])
            visited.add((i, j))

            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            while queue:
                r, c = queue.popleft()
                count += 1
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (nr in range(row) and
                       nc in range(col) and
                       grid[nr][nc] == 1 and
                       (nr, nc) not in visited):

                       queue.append((nr, nc))
                       visited.add((nr, nc))
            if count > self.max_area:
                self.max_area = count

        self.max_area = 0        
        row, col = len(grid), len(grid[0])
        visited = set()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i, j) not in visited:
                    bfs(i, j)
        return self.max_area

        