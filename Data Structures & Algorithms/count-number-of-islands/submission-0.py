class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(i, j):
            q = collections.deque([(i, j)])
            visited.add((i, j))

            while q:
                current = q.popleft()
                x, y = current

                if (x > 0 and 
                (x - 1, y) not in visited and 
                grid[x - 1][y] == "1"):
                    q.append((x - 1, y))
                    visited.add((x - 1, y))
                
                if (y > 0 and 
                (x, y - 1) not in visited and 
                grid[x][y - 1] == "1"):
                    q.append((x, y - 1))
                    visited.add((x, y - 1))

                if (x < row - 1 and
                    (x + 1, y) not in visited and
                    grid[x + 1][y] == "1"):
                    q.append((x + 1, y)) 
                    visited.add((x + 1, y))  

                if (y < col - 1 and
                   (x, y + 1) not in visited and
                   grid[x][y + 1] == "1"):
                    q.append((x, y + 1))   
                    visited.add((x, y + 1))

        row, col = len(grid), len(grid[0])
        visited = set()
        islands = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1
        return islands
