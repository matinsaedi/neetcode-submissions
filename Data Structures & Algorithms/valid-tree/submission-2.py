class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = {i:[] for i in range(n)}
        """
        graph = {0: [1, 2, 3], 1: [0, 4], 2: [0], 3: [0], 4: [1]}
        """

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        visited = set()

        def dfs(node, par):
            if node in visited:
                return True

            visited.add(node)

            for nei in graph[node]:
                if nei == par:
                    continue

                if nei in visited:
                    return False

                if not dfs(nei, node):
                    return False
            
            return True

        
        return dfs(0, -1) and len(visited) == n            