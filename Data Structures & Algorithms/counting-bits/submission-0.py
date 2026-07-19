class Solution:
    def countBits(self, n: int) -> List[int]:

        def helper(n: int) -> int:
            c = 0

            for i in range(32):
                if n & (1 << i):
                    c += 1

            return c

        res = []
        for i in range(n+1):
            res.append(helper(i))

        return res
        