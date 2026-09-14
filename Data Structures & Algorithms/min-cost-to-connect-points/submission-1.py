class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        points = [tuple(p) for p in points]
        visited = set()
        min_heap = [(0, points[0])]
        total_cost = 0

        while points:
            cost, point = heapq.heappop(min_heap)

            if point in visited:
                continue

            visited.add(point)
            total_cost += cost

            points.remove(point)

            for p in points:
                if p not in visited:
                    weight = abs(point[0] - p[0]) + abs(point[1] - p[1])
                    heapq.heappush(min_heap, (weight, p))

        return total_cost