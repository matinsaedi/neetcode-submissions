class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = {i : [] for i in range(n)}
        """ graph = {0: [1], 
                    1: [0, 2], 
                    2: [1], 
                    3: [4], 
                    4: [3]}
        """

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        visited = set()
        self.components = n

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for nei in graph[node]:
                dfs(nei)

        components = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1

        return components