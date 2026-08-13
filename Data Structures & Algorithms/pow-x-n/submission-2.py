class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1

        if n < 0:
            return self.myPow(1/x, -n)

        if n % 2 == 0:
            tmp = self.myPow(x, n // 2)
            return tmp * tmp
        else:
            tmp = self.myPow(x, n // 2)
            return x * tmp * tmp

        