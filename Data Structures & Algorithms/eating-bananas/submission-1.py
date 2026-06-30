import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        output = 0

        while l <= r:
            k = (l + r) // 2

            res = 0
            for p in piles:
                res += math.ceil(p / k)

            if res > h:
                l = k + 1
                continue

            elif res <= h:
                r = k - 1
                output = k
                continue

        return output