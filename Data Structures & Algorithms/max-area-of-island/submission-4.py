class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def bfs(i, j):
            count = 0
            queue = collections.deque([(i, j)])
            visited.add((i, j))

            while queue:
                r, c = queue.popleft()
                count += 1
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (0 <= nr < row and
                        0 <= nc < col and
                       grid[nr][nc] == 1 and
                       (nr, nc) not in visited):

                       queue.append((nr, nc))
                       visited.add((nr, nc))
            return count
            
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        max_area = 0        
        row, col = len(grid), len(grid[0])
        visited = set()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i, j) not in visited:
                    count = bfs(i, j)
                    max_area = max(max_area, count)
        return max_area