class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        l, r = 0, n - 1

        while l < r:
            for i in range(l, r):
                (matrix[l][i], matrix[i][r], matrix[r][l + r - i], matrix[l + r - i][l]) = (matrix[l + r - i][l], matrix[l][i], matrix[i][r], matrix[r][l + r - i])
            
            l += 1
            r -= 1
