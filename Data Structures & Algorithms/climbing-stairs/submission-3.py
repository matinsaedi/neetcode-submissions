class Solution:
    def climbStairs(self, n: int) -> int:

        o1, o2 = 1, 1

        for i in range(n - 1):
            tmp = o2
            o2 = o1 + o2
            o1 = tmp
        
        return o2