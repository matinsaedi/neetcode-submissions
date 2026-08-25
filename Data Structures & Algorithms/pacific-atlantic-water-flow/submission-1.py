class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        row, col = len(heights), len(heights[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # pacific
        qp = collections.deque()
        pacific = set()
        for i in range(row):
            for j in range(col):
                if i == 0 or j == 0:
                    pacific.add((i, j))
                    qp.append((i, j))

        # atlantic
        qa = collections.deque()
        atlantic = set()
        for i in range(row):
            for j in range(col):
                if i == row - 1 or j == col - 1:
                    atlantic.add((i, j))
                    qa.append((i, j))

        while qp:
            r, c = qp.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < row and
                    0 <= nc < col and
                    heights[nr][nc] >= heights[r][c] and
                    (nr, nc) not in pacific):
                    pacific.add((nr, nc))
                    qp.append((nr, nc))

        while qa:
            r, c = qa.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < row and
                    0 <= nc < col and
                    heights[nr][nc] >= heights[r][c] and
                    (nr, nc) not in atlantic):
                    atlantic.add((nr, nc))
                    qa.append((nr, nc))

        return list([i, j] for i, j in (pacific & atlantic))






