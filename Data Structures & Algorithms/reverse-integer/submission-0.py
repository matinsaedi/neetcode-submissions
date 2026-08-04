class Solution:
    def reverse(self, x: int) -> int:
        
        max_num = 2 ** 31 - 1
        min_num = -2 ** 31
        
        sign = 1
        if x < 0:
            sign = -1

        x = abs(x)    
        res = 0
        while x != 0:
            y = x % 10 
            x //= 10

            res = res * 10 + y

        if (res // 10) > (max_num // 10):
            return 0
        
        if res // 10 == max_num // 10:
            if res % 10 > max_num % 10:
                return 0

        return res * sign

