class Solution:
    def isHappy(self, n: int) -> bool:

        def sumSquares(n):
            res = 0
            while n > 0:
                digit = n % 10
                res += digit ** 2

                n //= 10

            return res

        hash_set = set()

        while n != 1:
            n = sumSquares(n)
            if n in hash_set:
                return False

            hash_set.add(n)

        return True

        