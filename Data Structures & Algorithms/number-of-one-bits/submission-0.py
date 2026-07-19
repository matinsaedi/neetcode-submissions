class Solution:
    def hammingWeight(self, n: int) -> int:
        
        bit = 1
        c = 0

        for i in range(32):
            if n & (bit << i):
                c += 1

        return c