class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        candidates = []
        for x, y, z in triplets:
            if x > target[0] or y > target[1] or z > target[2]:
                continue
            candidates.append([x, y, z])

        fx, fy, fz = False, False, False
        for x, y, z in candidates:
            if x == target[0]:
                fx = True

            if y == target[1]:
                fy = True
            
            if z == target[2]:
                fz = True

        return fx and fy and fz