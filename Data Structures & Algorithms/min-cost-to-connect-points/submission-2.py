class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []

        for i in range(n):
            for j in range(i + 1, n):
                distance = (abs(points[i][0] - points[j][0]) + 
                            abs(points[i][1] - points[j][1]))
                edges.append((distance, i, j))

        edges.sort()

        parent = [i for i in range(n)]
        rank = [1] * n


        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]


        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False

            if rank[root_a] < rank[root_b]:
                root_a, root_b = root_b, root_a
            
            parent[root_b] = root_a
            rank[root_a] += rank[root_b]

            return True

        total_cost = 0
        total_edges = 0
        for weight, i, j in edges:
            
            if total_edges == (n - 1):
                break

            if union(i, j):
                total_cost += weight
                total_edges += 1
            else:
                continue

        return total_cost


        