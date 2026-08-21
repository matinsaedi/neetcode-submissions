import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        data = [-i for i in stones]
        heapq.heapify(data)

        while len(data) > 1:
            y = - heapq.heappop(data)
            x = - heapq.heappop(data)

            if x < y:
                heapq.heappush(data, -(y - x))

        return - data[0] if data else 0