class Solution:
    def reverse(self, x: int) -> int:
        
        max_num = 2 ** 31 - 1
        min_num = -2 ** 31
        
        sign = -1 if x < 0 else 1
        x = abs(x)   

        res = 0

        while x:
            digit = x % 10 
            x //= 10

            if ((res > max_num // 10) or
            res == max_num // 10 and digit > max_num % 10):
                return 0

            res = res * 10 + digit

        return res * sign

