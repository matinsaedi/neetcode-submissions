class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        minutes = -1
        row, col = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = collections.deque([])

        rotten_count = 0
        fresh_count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    rotten_count += 1
                elif grid[i][j] == 1:
                    fresh_count += 1

        if rotten_count == 0:
            if fresh_count == 0:
                return 0
            else:
                return -1

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j))

        while queue:
            current_level = len(queue)
            for level in range(current_level):
                r, c = queue.popleft()
                grid[r][c] = 0

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (0 <= nr < row and
                        0 <= nc < col and
                        grid[nr][nc] == 1):
                        queue.append((nr, nc))
                        grid[nr][nc] = 2 
            minutes += 1

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1

        return minutes




                       
