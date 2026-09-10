class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = {i: [] for i in range(1, n + 1)}
        for i, j, w in times:
            graph[i].append((j, w))

        #   graph = {1: [(2, 1), (4, 4)], 
        #            2: [(3, 1)], 
        #            3: [(4, 1)], 
        #            4: []}

        distances = {node: float("inf") for node in graph}
        distances[k] = 0

        min_heap = [(0, k)]

        while min_heap:
            current_dist, node = heapq.heappop(min_heap)

            # if current_dist > distances[node]:
            #     continue

            for neighbor, weight in graph[node]:
                new_dist = weight + current_dist

                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(min_heap, (new_dist, neighbor))


        max_dist = max(distances.values())
        return max_dist if max_dist != float("inf") else -1
