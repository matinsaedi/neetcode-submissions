class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        o1, o2 = 0, 0

        for i in range(2, len(cost) + 1):
            tmp = o2
            o2 = min(o2 + cost[i - 1],
                     o1 + cost[i - 2])
            o1 = tmp

        return o2
        