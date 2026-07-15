class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1

        o1 = 1
        o2 = 1

        res = 0
        for i in range(n - 1):
            res = o1 + o2

            o1 = o2
            o2 = res

        return res