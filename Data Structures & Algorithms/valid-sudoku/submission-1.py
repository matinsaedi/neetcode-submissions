class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Row check
        
        for i in range(9):
            visited = set()
            row = board[i]
            for val in row:
                if val != ".":
                    if val in visited:
                        return False
                    
                    visited.add(val)

        # Column check
        for j in range(9):
            visited = set()
            for i in range(9):
                val = board[i][j]
                if val != ".":
                    if val in visited:
                        return False
                    
                    visited.add(val)

        # 3*3 Box check
        for start_row in range(0, 9, 3):
            for start_column in range(0, 9, 3):
                visited = set()
                for i in range(start_row, start_row+3):
                    for j in range(start_column, start_column+3):
                        val = board[i][j]
                        if val != ".":
                            if val in visited:
                                return False
                            
                            visited.add(val)

        return True


        

        
        