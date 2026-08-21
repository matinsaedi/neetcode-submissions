class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        candidates = []
        for i in range(k):
            x = points[i][0]
            y = points[i][1]
            d = x ** 2 + y ** 2
            candidates.append([-d, [x, y]])

        heapq.heapify(candidates)
        if k < len(points):
            for i in range(k, len(points)):
                x = points[i][0]
                y = points[i][1]
                d = x ** 2 + y ** 2

                if -d > candidates[0][0]:
                    heapq.heappop(candidates)
                    heapq.heappush(candidates, [-d, [x, y]])

        return [c[1] for c in candidates]


                

        