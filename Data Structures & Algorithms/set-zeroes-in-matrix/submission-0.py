class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        m = len(matrix)
        n = len(matrix[0])

        hash_set = {'row': set(), 'col': set()}

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i not in hash_set['row']:
                        hash_set['row'].add(i)
                    
                    if j not in hash_set['col']:
                        hash_set['col'].add(j)

        for i in hash_set['row']:
            for j in range(n):
                matrix[i][j] = 0

        for j in hash_set['col']:
            for i in range(m):
                matrix[i][j] = 0
