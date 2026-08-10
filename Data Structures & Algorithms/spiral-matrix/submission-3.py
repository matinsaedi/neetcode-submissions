class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []

        l, r = 0, n - 1
        t, b = 0, m - 1

        while l < r and t < b:
            for i in range(l, r + 1):
                res.append(matrix[t][i])

            for j in range(t + 1, b + 1):
                res.append(matrix[j][r])

            for i in range(r - 1, l - 1, -1):
                res.append(matrix[b][i])

            for j in range(b - 1, t, -1):
                res.append(matrix[j][l])
            
            l += 1
            r -= 1
            t += 1
            b -= 1


        if t == b:
            for i in range(l, r + 1):
                res.append(matrix[t][i])

        elif l == r:
            for j in range(t, b + 1):
                res.append(matrix[j][r])

        return res