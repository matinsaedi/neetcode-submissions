class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {i: [] for i in range(numCourses)}
        # graph = {0:[], 1:[], 2:[], 3:[], 4:[]}

        for i, j in prerequisites:
            graph[j].append(i)

        visiting = set()
        visited = set()

        def dfs(node):
            if not graph[node]:
                return True
            
            if node in visited:
                return True

            if node in visiting:
                return False

            visiting.add(node)
            
            for course in graph[node]:
                if not dfs(course):
                    return False

            visiting.remove(node)
            visited.add(node)

            return True
         

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
            