class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        row, col = len(heights), len(heights[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, v):
            if r < 0 or c < 0 or r == row or c == col or (r, c) in v:
                return

            v.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < row and
                    0 <= nc < col and
                    heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, v)

        pacific = set()
        atlantic = set()
        for i in range(row):
            for j in range(col):
                if i == 0 or j == 0:
                    dfs(i, j, pacific)
                    
                if i == row - 1 or j == col - 1:
                    dfs(i, j, atlantic)

            
        return list([i, j] for i, j in (pacific & atlantic))