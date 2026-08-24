class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        m, n = len(board), len(board[0])
        q = collections.deque()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for i in range(m):
            for j in range(n):
                if ((i == 0 or i == m - 1) or (j == 0 or j == n - 1)) and board[i][j] == "O":
                    board[i][j] = "T"
                    q.append((i, j))
                 

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < m and
                   0 <= nc < n and
                   board[nr][nc] == "O"
                   ):
                   board[nr][nc] = "T"
                   q.append((nr, nc))
    

        for i in range(m):
            for j in range(n):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"


#
# board=[["O","X","X","O","X"],
#       ["X","O","O","X","O"],
#       ["X","O","X","O","X"],
#       ["O","X","O","O","O"],
#       ["X","X","O","X","O"]]
# 
    # [["O","X","X","O","X"],
    # ["X","X","X","X","O"]
    # ,["X","X","X","O","X"],
    # ["O","X","O","O","O"],
    # ["X","X","O","X","O"]]


    # [["O","X","X","O","X"],
    # ["X","X","X","X","O"],
    # ["X","X","X","X","X"],
    # ["O","X","O","O","O"],
    # ["X","X","O","X","O"]]
#