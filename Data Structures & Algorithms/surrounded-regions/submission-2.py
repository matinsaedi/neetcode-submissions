class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        q = collections.deque([])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        m, n = len(board), len(board[0])
        safe = set()

        for i in range(m):
            if board[i][0] == "O" and (i, 0) not in safe:
                safe.add((i, 0))
                q.append((i, 0))
            if board[i][-1] == "O" and (i, n-1) not in safe:
                safe.add((i, n - 1))
                q.append((i, n - 1))

        for j in range(n):
            if board[0][j] == "O" and (0, j) not in safe:
                safe.add((0, j))
                q.append((0, j))
            if board[-1][j] == "O" and (m-1, j) not in safe:
                safe.add((m - 1, j))
                q.append((m - 1, j))

                 
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < m and
                   0 <= nc < n and
                   board[nr][nc] == "O" and
                   (nr, nc) not in safe):
                   q.append((nr, nc))
                   safe.add((nr, nc))

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i, j) not in safe:
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