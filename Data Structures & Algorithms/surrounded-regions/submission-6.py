class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        m, n = len(board), len(board[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(r, c):
            if r < 0 or c < 0 or r == m or c == n or board[r][c] != "O":
                return
            
            board[r][c] = "T"

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and
                   0 <= nc < n and
                   board[nr][nc] == "O"
                   ):
                    dfs(nr, nc)

            
        for i in range(m):
            for j in range(n):
                if ((i == 0 or i == m - 1) or (j == 0 or j == n - 1)) and board[i][j] == "O":
                    dfs(i, j)
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"